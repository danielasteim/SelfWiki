from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search_results, name="search_results"),
    path("wiki/<str:title>", views.entry_pages, name="entry_pages"),
    path("newpage/", views.new_page, name="new_page"),
    path("editpage/<str:title>", views.edit_page, name="edit_page"),
    path("randompage", views.random_page, name="random_page")
]
