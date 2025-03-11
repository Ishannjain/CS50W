from django.shortcuts import render
import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def convert_to_html(title):
    content=util.get_entry(title)
    markdowner=markdown.Markdown()
    if content is None:
        return None
    else:
        return markdowner.convert(content)
def entry(request,title):
    html_converter=convert_to_html(title)
    if html_converter==None:
        return render(request,"encyclopedia/error.html",{
            "message":"Error page not found"
        })
    else:
        return render(request,"encyclopedia/entry.html",{
            "title":title,
            "content":html_converter
        })
def search(request):
    if request.method == "POST":
        entry_search=request.POST['q']
        html_converter=convert_to_html(entry_search)
        if html_converter is not None:
            return render(request,"encyclopedia/entry.html",{
                "title":entry_search,
                "content":html_converter
            })
        else:
            allEntries=util.list_entries()
            recomendations=[]
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recomendations.append(entry) 
            
            return render(request,"encyclopedia/search.html",{
                    "recomendations":recomendations
                         })
def new_page(request):
    if request.method == "GET":
        return render(request,"encyclopedia/new_page.html")
    else:
        title=request.POST['title']
        content=request.POST['content']
        titleExist=util.get_entry(title)
        if titleExist is not None:
            return render(request,"encyclopedia/error.html",{
                "message":"Entry Page Already Exist"
            })
        else:
            util.save_entry(title,content) #to save the title in util.py
            html_content=convert_to_html(titles,content)
            return render(request,"encyclopedia/entry.html",{
                "title":title,
                "content":html_content
            })
def edit_page(request):
    if request.method == "POST":
       title=request.POST['enrty_title']
       content=util.get_entry(title)
      
       return render(request,"encyclopedia/edit_page.html",{
             "title":title,
             "content":html_content
             })
def save_entry(request):
        if request.method=="POST":
            title=request.POST['title']
            content=request.POST['content']
            util.save_entry(title,content)
            html_content=convert_to_html(title)
            return render(request,"encyclopedia/entry.html",{
                "title":title,
                "content":html_content
            })

