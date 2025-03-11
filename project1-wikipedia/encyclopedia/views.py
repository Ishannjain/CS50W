from django.shortcuts import render
import markdown # pip3 install markdown2
import  random
from . import util
#WORKING OF FUNCTION: we conerting md to html using markdown converter
def converter_md_to_html(title):
       content=util.get_entry(title)
       markdowner=markdown.Markdown()
       if content==None:# if title dosen't exist then return none
           return None
       else:
            return  markdowner.convert(content)# if existso we convert it into md ->html


def index(request):
    
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# here we completed our entry portion with error and entry message
def entry(request,title):
     html_content=converter_md_to_html(title)
     if html_content==None:
        return render(request, "encyclopedia/error.html",{
            "message":"This entry dosen't exist"
        })
     else:
        return render(request, "encyclopedia/entry.html",{
            "title":title,
            "content":html_content
        })
#for search

def search(request):
    if request.method == "POST":
        entry_search=request.POST['q']
        html_content=converter_md_to_html(entry_search)
        if(html_content is not None):
            return render(request, "encyclopedia/entry.html",{
            "title":entry_search,
            "content":html_content
        })
        else:
        #   variable for all entries
            allEntries=util.list_entries() 
            recommendation=[]
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html",{
                "recommendation":recommendation
            })
            # function for new page
def new_page(request):
    if request.method=="GET":
        return render(request,"encyclopedia/new.html")
    else:
        title=request.POST['title']
        content=request.POST['content']
        titleExist=util.get_entry(title)
        if  titleExist is not None:
            return render(request,"encyclopedia/error.html",{
                "message":"Entry Page Already Exist"
            })
        else:
            util.save_entry(title,content)
            html_content=converter_md_to_html(title)
            return render(request,"encyclopedia/entry.html",{
                "title":title,
                "content":html_content
            })
            # for edit 

def edit(request):
    if request.method=="POST":
        title=request.POST['entry_title']
        content=util.get_entry(title)
        return render(request,"encyclopedia/edit.html",{
            "title":title,
            "content":content
        })
        # for save the data
def save_edit(request):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']

        util.save_entry(title,content)
        html_content=converter_md_to_html(title)
        return render(request,"encyclopedia/entry.html",{
                "title":title,
                "content":html_content
            })

def rand(request):
    allEntries=util.list_entries()
    rand_entry= random.choice(allEntries)
    html_content=converter_md_to_html(rand_entry)
    return render(request,"encyclopedia/entry.html",{
        "title":rand_entry,
        "content":html_content
    })