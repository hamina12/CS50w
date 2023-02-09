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
    if request.method == "POST":
        name = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            "title" : title,
            "text" : name
        })

    try:
        name = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/entry.html", {
            "title" : name
        })
    except:
        name = "Request page not found"
        return render(request, "encyclopedia/entry.html", {
            "title" : name
        })



def create(request):
    if request.method == "POST":
        if 'q' in request.POST:
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

        elif 'text' in request.POST and 'text' in request.POST:
            util.save_entry(request.POST.get('title'), request.POST.get('text'))
            name = markdown2.markdown(util.get_entry(request.POST.get('title')))
            return render(request, "encyclopedia/entry.html", {
                "title" : name
            })

    return render(request, "encyclopedia/create.html")

def edit(request):
    if request.method == "POST":
        if 'q' in request.POST:
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
        #if 'text' in request.POST:


    return render(request, "encyclopedia/edit.html")




