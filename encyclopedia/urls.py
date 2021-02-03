from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:entry_title>/", views.entry, name="entry")
]
