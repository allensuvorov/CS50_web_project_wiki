from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>/", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("random", views.random_page, name="random"),
    path("new", views.new, name="new"),
    path("<str:title>/edit", views.edit, name="edit")
    # To design URLs for an app, you create a Python module informally called a URLconf (URL configuration).
]
