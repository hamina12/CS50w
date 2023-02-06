from django.shortcuts import render
import random
from . import util


def index(request):
    entri = util.list_entries()
    if request.method == "POST":
        return render(request, "encyclopedia/load.html",{
            
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
        "random" : util.get_entry(entri[n])
    })

