


### THINGS I LEARNED FROM THIS PROJECT

* With django when rendering a page you can return a string and transform it on actual html for a page using the 'safe' keyword. "html": "<p>string</p>" and use it dynamically on the page as {{ html|*safe* }}, 

* It's possible to create dynamic URL's using <parameter> when defining the route, and the using this parameter on the function of the view.
```python
# ON URLS.PY
path("wiki/<str:title>", views.entry_pages, name="entry_pages")
# ON VIEWS.PY
def entry_pages(request, title):
```

* With a dynamic url its possible to use it on the html pages. On this project that was used so each html page for each entry would only be generated when the link was clicked or accesssed on wiki/{title}. 
```html
{% for entry in matching_entries %}
    <li><a href="{% url 'entry_pages' entry %}">{{ entry }}</a></li>
```

* That was only possible with the [markdown2](https://github.com/trentm/python-markdown2) library, which easily transforms .md files into string html.

* You can use forms to 'call' functions when its submitted, by having a url setted to a view function, and then adding that url to the action attributed of the form.
```python
# FORMS ON HTML PAGE
<form action="{% url 'search_results' %}" method="post">
    {% csrf_token %}
    <input class="search" type="text" name="q" placeholder="Search Encyclopedia">
</form>

# ON URLS.PY
path("search/", views.search_results, name="search_results"),

# ON VIEWS.PY
def search_results(request):
    if request.method == "POST":
        search_query = request.POST.get('q', '') # THIS IS HOW TO GET THE VALUE OF THE POST, Q BEING THE NAME OF INPUT FIELD
        # finish implementation
    
```

* You can import functions from util file with <from encyclopedia.util import get_entry, list_entries, save_entry>

