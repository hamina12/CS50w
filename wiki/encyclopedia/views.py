from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    infor = util.get_entry(title)
    return render(request, "encyclopedia/entry.html", {
        "infor" : infor,
        "title" : title
    })
