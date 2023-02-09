from django.shortcuts import render
import markdown2
import random
from . import util

def get_entry_or_search_results(request):
    q = request.POST.get('q')
    try:
        name = markdown2.markdown(util.get_entry(q))
        return render(request, "encyclopedia/entry.html", {
            "title": name,
            "send": q
        })
    except:
        ent = []
        entries = util.list_entries()
        for entry in entries:
            if q in entry:
                ent.append(entry)
        return render(request, "encyclopedia/search.html", {
            "entries": ent
        })

def index(request):
    if request.method == "POST":
        return get_entry_or_search_results(request)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entries = util.list_entries()
    if title in entries:
        name = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/entry.html", {
            "title": name,
            "send": title
        })
    else:
        name = "Requested page not found"
        return render(request, "encyclopedia/error.html", {
            "title": name
        })

def create(request):
    if request.method == "POST":
        if 'q' in request.POST:
            return get_entry_or_search_results(request)
        elif 'title' in request.POST and 'text' in request.POST:
            title = request.POST.get('title')
            text = request.POST.get('text')
            util.save_entry(title, text)
            name = markdown2.markdown(util.get_entry(title))
            return render(request, "encyclopedia/entry.html", {
                "title": name,
                "send": title
            })

    return render(request, "encyclopedia/create.html")

def edit(request, title):
    if request.method == "POST":
        if 'q' in request.POST:
            return get_entry_or_search_results(request)
        elif 'text' in request.POST:
            text = request.POST.get('text')
            util.save_entry(title, text)
            name = markdown2.markdown(util.get_entry(title))
            return render(request, "encyclopedia/entry.html", {
                "title": name,
                "send": title
            })

    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "text": util.get_entry(title),
    })

def randompage(request):
    if request.method == "POST":
        return get_entry_or_search_results(request)

    entries = util.list_entries()
    random_entry_title = random.choice(entries)
    name = markdown2.markdown(util.get_entry(random_entry_title))

    return render(request, "encyclopedia/entry.html", {
        "title": name,
        "send": random_entry_title
    })