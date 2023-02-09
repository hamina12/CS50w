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
                "title" : name,
                "send" : q
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
        name = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/entry.html", {
            "title" : name,
            "send" : title
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
                    "title" : name,
                    "send" : q
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

        elif 'title' in request.POST and 'text' in request.POST:
            util.save_entry(request.POST.get('title'), request.POST.get('text'))
            name = markdown2.markdown(util.get_entry(request.POST.get('title')))
            return render(request, "encyclopedia/entry.html", {
                "title" : name,
                "send" : request.POST.get('title')
            })

    return render(request, "encyclopedia/create.html")

def edit(request, title):
    if request.method == "POST" and 'text' in request.POST:
        text = request.POST.get('text')
        util.save_entry(title, text)
        name = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/entry.html", {
            "title" : name,
            "send" : title
        })

    if request.method == "POST" and 'q' in request.POST:
        q = request.POST.get('q')
        try:
            name = markdown2.markdown(util.get_entry(q))
            return render(request, "encyclopedia/entry.html", {
                "title" : name,
                "send" : q
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

    return render(request, "encyclopedia/edit.html", {
        "title" : title,
        "text" : util.get_entry(title),
    })

def randompage(request):
    if request.method == "POST" and 'q' in request.POST:
        q = request.POST.get('q')
        try:
            name = markdown2.markdown(util.get_entry(q))
            return render(request, "encyclopedia/entry.html", {
                "title" : name,
                "send" : q
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

    entri = util.list_entries()
    n = random.randrange(len(entri))
    send = entri[n]
    name = markdown2.markdown(util.get_entry(entri[n]))
    return render(request, "encyclopedia/entry.html", {
        "title" : name,
        "send" : send
    })

