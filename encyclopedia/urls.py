from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:entry>/", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("random", views.random_page, name="random"),
    path("new", views.new, name="new"),
    path("wiki/<str:title>/edit", views.edit, name="edit")
    # To design URLs for an app, you create a Python module informally called a URLconf (URL configuration).
]
