from django.shortcuts import render
from django import forms 

from . import util

class SearchForm(forms.Form):
    query = forms.CharField(label="Search Encyclopedia")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": SearchForm()
    })

def entry(request, entry):
    if util.get_entry(entry) is None:
        return render(request, "encyclopedia/error.html", {
            "content": "page not found"
            }) 
    return render(request, "encyclopedia/entry.html", {
        "entry": entry, 
        "content": util.get_entry(entry)
        })

# search for entry
def search(request):
    return render(request, "encyclopedia/search.html")
