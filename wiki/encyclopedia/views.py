from django.shortcuts import render
from django import forms
import random
from . import util


def index(request):
    if request.method == "POST":
        name = request.POST.get('q')
        return render(request, "encyclopedia/load.html",{
            "head" : name,
            "infor" : util.get_entry(name)
        })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def save(request):
    if request.method == "POST":
        name = request.POST.get('q')
        text = request.POST.get('text')
        title = request.POST.get('title')
        if text.is_valid():
            return render(request, "encyclopedia/load.html",{
                "head" : name,
                "infor" : util.get_entry(name)
            })
        elif text != None and title != None:
            util.save_entry(title, text)
            return render(request, "encyclopedia/load.html",{
                "head" : title,
                "infor" : util.get_entry(title)
            })
        else:
            return render(request, "encyclopedia/save.html")
    return render(request, "encyclopedia/save.html")


def load(request):
    if request.method == "POST":
        name = request.POST.get('q')
        return render(request, "encyclopedia/load.html",{
            "head" : name,
            "infor" : util.get_entry(name)
        })
    entri = util.list_entries()

    n = random.randrange(len(entri))
    return render(request, "encyclopedia/load.html", {
        "head" : entri[n],
        "infor" : util.get_entry(entri[n])
    })

