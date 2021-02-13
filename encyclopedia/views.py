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
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            
            # Isolate the task from the 'cleaned' version of form data
            query = form.cleaned_data["query"] # what's that?

            # if query matches entry title
            if util.get_entry(query):
                return entry(request, query)
            else:
                # search for query as substring
                found = []
                for article in util.list_entries():
                    # print (query, util.get_entry(article)) 
                    if query.lower() in util.get_entry(article).lower():
                        found.append(article)

                return render(request, "encyclopedia/search.html", {
                    "found": found,
                    "query": query
                })
