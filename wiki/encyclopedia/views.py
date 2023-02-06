from django.shortcuts import render
import randrange
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
        "random" : util.get_entry(entri[randrange(len(entri))])
    })

