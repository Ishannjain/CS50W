from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User,Category,Listing,Comment,Bid

def listing(request,id):
    # collecting data from database by using primary key as a id
    listingData=Listing.objects.get(pk=id)
    isListingInWatchList=request.user in listingData.watchlist.all()
    allComments=Comment.objects.filter(listing=listingData)
    isOwner=request.user.username==listingData.owner.username
    return render(request,"auctions/listing.html",{
        "listing":listingData,
        "isListing":isListingInWatchList,
        "allComments":allComments,
        "isowner":isOwner
        })

def closeauction(request,id):
    listingData=Listing.objects.get(pk=id)
    listingData.isActive=False
    listingData.save()
    isListingInWatchList=request.user in listingData.watchlist.all()
    allComments=Comment.objects.filter(listing=listingData)
    isOwner=request.user.username==listingData.owner.username 
    return render(request,"auctions/listing.html",{
        "listing":listingData,
        "isListing":isListingInWatchList,
        "allComments":allComments,
        "iswner":isOwner,
        "update":True,
        "message":"Sorry! Your auction is closed"
    })
def displayWatchlist(request):
    currentUser=request.user
    listings=currentUser.listingWatchlist.all()
    return render(request,"auctions/watchlist.html",{
        "listings":listings
    })
    
def removeWatchList(request,id):
    listingData=Listing.objects.get(pk=id)
    currentUser=request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing",args=(id,)))
def addWatchList(request,id):
    listingData=Listing.objects.get(pk=id)
    currentUser=request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing",args=(id,)))
def addBid(request,id):
    newBid=request.POST['newBid']
    listingData=Listing.objects.get(pk=id)
    isListingInWatchList=request.user in listingData.watchlist.all()
    allComments=Comment.objects.filter(listing=listingData)
    isOwner=request.user.username==listingData.owner.username
    if int(newBid)>listingData.price.bid:
        updateBid=Bid(user=request.user,bid=int(newBid))
        
        updateBid.save()
        listingData.price=updateBid
        listingData.save()
        
        return render(request, 'auctions/listing.html',{
            "listing":listingData,
            "message":"Bid was Updated Successfully",
            "update":True,
            "isListing":isListingInWatchList,
            "allComments":allComments,
            "isowner":isOwner
        })
    else:
        return render(request, 'auctions/listing.html',{
            "listing":listingData,
            "message":"Bid was  updated failed",
            "update":False,
            "isListing":isListingInWatchList,
            "allComments":allComments,
            "isowner":isOwner
        })
def addComment(request,id):
    currentUser=request.user
    listingData=Listing.objects.get(pk=id)
    message=request.POST['newComment']
    newComment = Comment(
        author=currentUser,
        listing=listingData,
        message=message
    )
    newComment.save()
    return HttpResponseRedirect(reverse("listing",args=(id,)))

def index(request):
    # to check the listings
    allCategories =Category.objects.all()
    activeListings =Listing.objects.filter(isActive=True)
    return render(request, "auctions/index.html",{
        "Listings":activeListings,
        "categories":allCategories
    })
# to select the category
def displayCategory(request):
    if request.method =="POST":
        categoryFromForm=request.POST['category']
        category=Category.objects.get(categoryName=categoryFromForm)
        allCategories =Category.objects.all()
        activeListings =Listing.objects.filter(isActive=True,category=category)
        return render(request, "auctions/index.html",{
            "Listings":activeListings,
            "categories":allCategories
        })
def createListing(request):
    # get method for data which we created
    if request.method =="GET":
        # to listing it with page
        allCategories =Category.objects.all()
        return render(request, "auctions/create.html",{
            "categories":allCategories
        })
    else:
        # for post method
        # get the data from the form
        title = request.POST["title"]
        description = request.POST["description"]
        imageurl = request.POST["imageurl"]
        price = request.POST["price"]
        category = request.POST["category"]

        # who is the user
        currentUser=request.user
        # get all content  about the particular category
        categoryData=Category.objects.get(categoryName=category)
        # create a bid object 
        bid=Bid(bid=int(price),user=currentUser)
        bid.save()
        # create a new listing objects 
        newListing=Listing(
            title=title,
            description=description,
            imageUrl=imageurl,
            price=bid,
            category=categoryData,
            owner=currentUser
        )
        # Insert the object in our database
        newListing.save()
        # Redirect to index page
        return HttpResponseRedirect(reverse('index'))
        

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
