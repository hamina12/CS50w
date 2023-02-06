from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def save(request):
    return render(request, "encyclopedia/save.html", {

    })

def load(request):
    entri = util.list_entries()
    return render(request, "encyclopedia/load.html", {
        "entri" : entri[0],
        "random" : util.get_entry(entri[0])
    })

