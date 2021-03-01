from django.shortcuts import render
from django import forms 
from markdown2 import Markdown
import random

from . import util

class SearchForm(forms.Form):
    query = forms.CharField(
        widget = forms.TextInput(attrs={
            'class': 'search',
            'placeholder': 'Search Encyclopedia'
            }),
        label="Search")

class NewPageForm(forms.Form):
    title = forms.CharField(
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title'
        })
    )
    content = forms.CharField(
        widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'MarkDown Text'
        })
    )

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": SearchForm()
    })

def entry(request, entry):
    if util.get_entry(entry) is None:
        return render(request, "encyclopedia/error.html", {
            "content": "page not found",
            "form": SearchForm()
            })
    markdowner = Markdown() 
    return render(request, "encyclopedia/entry.html", {
        "entry": entry, 
        "content": markdowner.convert(util.get_entry(entry)),
        "form": SearchForm()
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
                    "query": query,
                    "form": SearchForm()
                })

# random page
def random_page(request):
    return entry(request, random.choice(util.list_entries()))

# new page
def new(request):

    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title):
                return render(request, "encyclopedia/error.html", {
                    "content": "page " + title + " already exists",
                    "form": SearchForm()
                    })
            util.save_entry(title, content)
            return entry(request, title)
    return render(request, "encyclopedia/new.html", {
        "new_page_form": NewPageForm(),
        "form": SearchForm()
    })

def edit(request, title):

    class EditPageForm(forms.Form):
        title_field = forms.CharField(
            widget = forms.TextInput(attrs={
                'class': 'form-control'
                # 'value': 'Title to edit'
            }),
            initial = title
        )
        content_field = forms.CharField(
            widget = forms.Textarea(attrs={
                'class': 'form-control',
                # 'value': 'MarkDown Text'
            }),
            initial = util.get_entry(title)
        )
    
    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            new_title = form.cleaned_data["title_field"]
            new_content = form.cleaned_data["content_field"]
            print(new_title, new_content)
            util.save_entry(new_title, new_content)
            return entry(request, new_title)

    return render(request, "encyclopedia/edit.html", {
        "edit_page_form": EditPageForm(),
        "form": SearchForm(),
        "title": title
    })