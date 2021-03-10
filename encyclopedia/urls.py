from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:entry>/", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("random", views.random_page, name="random"), # edit makes Request URL:	http://127.0.0.1:8000/edit
    path("new", views.new, name="new"),
    path("wiki/<str:title>/edit", views.edit, name="edit")
]
