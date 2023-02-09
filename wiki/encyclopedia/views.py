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
            name = "Requested page was not found."
            return render(request, "encyclopedia/entry.html", {
                "title" : name
            })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    try:
        name = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/entry.html", {
            "title" : name
        })
    except:
        name = "Requested page was not found."
        return render(request, "encyclopedia/entry.html", {
            "title" : name
        })

def randompage(request):
    if request.method == "POST":
        q = request.POST.get('q')
            try:
                name = markdown2.markdown(util.get_entry(q))
                return render(request, "encyclopedia/entry.html", {
                "title" : name
                })
            except:
                name = "Requested page was not found."
                return render(request, "encyclopedia/entry.html", {
                    "title" : name
                })

    entri = util.list_entries()
    n = random.randrange(len(entri))
    name = markdown2.markdown(util.get_entry(entri[n]))
    return render(request, "encyclopedia/entry.html", {
        "title" : name
    })

