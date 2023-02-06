from django.shortcuts import render
import random
from . import util

def index(request):
    if request.method == "POST":
        return render(request, "encyclopedia/load.html",{
            "head" : "CSS"
            "infor" : util.get_entry("CSS")
        })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def save(request):
    return render(request, "encyclopedia/save.html", {

    })

def load(request):
    entri = util.list_entries()
    n = random.randrange(len(entri))
    return render(request, "encyclopedia/load.html", {
        "head" : entri[n],
        "infor" : util.get_entry(entri[n])
    })

