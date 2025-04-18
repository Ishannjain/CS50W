from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry,name="entry"),
    path("search/",views.search, name="search"),
    path("new_page/",views.new_page,name="new_page"),
    path("edit_page/",views.edit_page,name="edit_page"),
    path("save_entry/",views.save_entry,name="save_entry")
]
