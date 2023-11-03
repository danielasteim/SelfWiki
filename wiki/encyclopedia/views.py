from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2
from . import util
from encyclopedia.util import get_entry, list_entries, save_entry
from random import choice


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search_results(request):
    if request.method == "POST":
        search_query = request.POST.get('q', '')
        matching_entry = get_entry(search_query)

        if matching_entry is not None:
            html = markdown2.markdown(matching_entry)
            return render(request, "encyclopedia/entry.html", {
                "title": search_query.capitalize(),
                "content": html
            })
        else:
            entries = list_entries()
            matching_entries = [entry for entry in entries if search_query in entry]

            if matching_entries:
                sorted_entries = sorted(matching_entries)
                return render(request, "encyclopedia/searchresults.html", {
                    "matching_entries": sorted_entries
                })
            else:
                # Handle the case where no matching entries are found
                return render(request, "encyclopedia/searchresults.html", {
                    "search_query": search_query
                })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })


def entry_pages(request, title):
    entry = get_entry(title) # SEARCHES FOR EXISTING ENTRY MATCHING TITLE

    if (entry != None): # IF ENTRY EXISTS RENDERS THE ENTRY PAGE
        html = markdown2.markdown(entry)
        return render(request, "encyclopedia/entry.html", {
            "title": title.capitalize,
            "content": html
        })
    else: 
        return render(request, "encyclopedia/error.html", {
            "message": "Requested page was not found"
        })

def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        title.capitalize

        # IF TITLE ALREADY EXISTS, SHOW ERROR MESSAGE
        entry_exists = get_entry(title)
        if entry_exists != None:
            return render(request, "encyclopedia/error.html", {
            "message": "Page already exists"
        })

        # ELSE SAVE ENTRY TO DISK AND REDIRECT TO PAGE
        else:
            content = request.POST.get("content", "")
            save_entry(title, content)
            content = get_entry(title)
            html = markdown2.markdown(content)
            return render(request, "encyclopedia/entry.html", {
                "title": title.capitalize,
                "content": html
            })
    else:
        return render(request, "encyclopedia/newpage.html")

def edit_page(request, title):
    if request.method == 'POST':
        content = request.POST.get("content", "")
        save_entry(title, content)
        content = get_entry(title)
        html = markdown2.markdown(content)
        return render(request, "encyclopedia/entry.html", {
            "title": title.capitalize,
            "content": html
        })
    else:
        content = get_entry(title)
        return render(request, "encyclopedia/editpage.html", {
            "content": content,
            "title": title
        })

def random_page(request):
    all_entries = list_entries()
    random_entry_title = choice(all_entries)
    random_entry_content = get_entry(random_entry_title)
    html = markdown2.markdown(random_entry_content)

    return render(request, "encyclopedia/entry.html", {
        "title": random_entry_title,
        "content": html
    })

