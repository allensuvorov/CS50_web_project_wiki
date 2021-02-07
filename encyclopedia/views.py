from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    # check if util.get_entry(entry) returns NONE then - render error.html
    
    return render(request, "encyclopedia/entry.html", {"entry": entry, "content": util.get_entry(entry)})
