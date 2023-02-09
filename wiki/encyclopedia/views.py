from django.shortcuts import render
import markdown2
import random
from . import util


def index(request):
    if request.method == "POST":
        q = request.POST.get('q')
        try:
            name = markdown2.markdown(util.get_entry(q))
            return render(request, "encyclopedia/entry.html", {
                "title" : name
            })
        except:
            ent = []
            entries = util.list_entries()
            for entri in entries:
                if q in entri:
                    ent.append(entri)
            return render(request, "encyclopedia/search.html", {
                "entries" : ent
            })


    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    try:
        name = markdown2.markdown(util.get_entry(q))
        return render(request, "encyclopedia/entry.html", {
            "title" : name
        })
    except:
        name = "Request page not found"
        return render(request, "encyclopedia/entry.html", {
            "title" : name
        })

def create(request):
    return render(request, "encyclopedia/create.html")



