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
    return render(request, "encyclopedia/load.html", {
        util.get_entry(util.list_entries(random()))
    })

