from django.shortcuts import render
import random
from . import util
import markdown2

def index(request):
    if request.method == "POST":
        name = request.POST.get('q')
        return render(request, "encyclopedia/load.html",{
            "infor" : markdown2.markdown(util.get_entry(name))
        })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def save(request):
    if request.method == "POST":
        if 'q' in request.POST:
            name = request.POST.get('q')
            return render(request, "encyclopedia/load.html",{
                "infor" : markdown2.markdown(util.get_entry(name))
            })

        elif 'title' != '':
            text = request.POST.get('text')
            title = request.POST.get('title')
            util.save_entry(title, text)
            return render(request, "encyclopedia/load.html",{
                # "infor" : markdown2.markdown(util.get_entry(title))
            })

    return render(request, "encyclopedia/save.html")


def load(request):
    if request.method == "POST":
        name = request.POST.get('q')
        return render(request, "encyclopedia/load.html",{
            "infor" : markdown2.markdown(util.get_entry(name))
        })

    entri = util.list_entries()
    n = random.randrange(len(entri))
    return render(request, "encyclopedia/load.html", {
        "infor" : markdown2.markdown(util.get_entry(entri[n]))
    })

