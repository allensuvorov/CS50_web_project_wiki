from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    if util.get_entry(entry) is None:
        return render(request, "encyclopedia/error.html", {"content": "page not found"}) 
    return render(request, "encyclopedia/entry.html", {"entry": entry, "content": util.get_entry(entry)})
