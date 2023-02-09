from django.shortcuts import render, get_object_or_404
import random
from . import util
import markdown2
from .models import EncyclopediaEntry

def index(request):
    if request.method == "POST":
        if 'q' in request.POST:
            name = request.POST.get('q')
            try:
                infor = markdown2.markdown(util.get_entry(name))
                return render(request, "encyclopedia/load.html",{
                    "infor" : infor
            })
            except:
                infor = "NONE"
                return render(request, "encyclopedia/load.html", {
                    "infor" : infor
                })
        else:
            return render(request, "encyclopedia/load.html")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, title):
    entry = get_object_or_404(EncyclopediaEntry, title=title)
    return render(request, 'encyclopedia/entry_page.html', {'entry': entry})

def save(request):
    if request.method == "POST":
        if 'text' in request.POST and 'text' in request.POST:
            title = request.POST.get('title')
            text = request.POST.get('text')
            util.save_entry(title, text)
            try:
                infor = markdown2.markdown(util.get_entry(title))
                return render(request, "encyclopedia/index.html",{
                    "entries": util.list_entries()
                })
            except:
                infor = "NOT EXIST"
                return render(request, "encyclopedia/load.html", {
                    "infor" : infor
                })

        if 'q' in request.POST:
            name = request.POST.get('q')
            try:
                infor = markdown2.markdown(util.get_entry(name))
                return render(request, "encyclopedia/load.html",{
                    "infor" : infor
            })
            except:
                infor = "NONE"
                return render(request, "encyclopedia/load.html", {
                    "infor" : infor
                })
    return render(request, "encyclopedia/save.html")


def load(request):
    if request.method == "POST":
        if 'q' in request.POST:
            name = request.POST.get('q')
            try:
                infor = markdown2.markdown(util.get_entry(name))
                return render(request, "encyclopedia/load.html",{
                    "infor" : infor
            })
            except:
                infor = "NONE"
                return render(request, "encyclopedia/load.html", {
                    "infor" : infor
                })

    entri = util.list_entries()
    n = random.randrange(len(entri))
    infor = markdown2.markdown(util.get_entry(entri[n]))
    return render(request, "encyclopedia/load.html", {
        "infor" : infor
    })