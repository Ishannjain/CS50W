from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from .models import User,Post,Follow,Like


def index(request):
    # to get the data of all post through database
    allPosts=Post.objects.all().order_by("id").reverse()
    allLikes=Like.objects.all()
    liked=[]
    try:
        for like in allLikes:
            if like.user.id==request.user.id:
                liked.append(like.post.id)
    except:
        liked=[]

    # pagination of django
    paginator=Paginator(allPosts,2)
    pgno=request.GET.get('page')
    post_page=paginator.get_page(pgno)
    return render(request, "network/index.html",{
        "allPosts":allPosts,
        "post_page":post_page,
        "liked":liked
    })


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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
    
def new_post(request):
    if request.method == "POST":
        Content=request.POST['Content']
        user=User.objects.get(pk=request.user.id)
        post=Post(Content=Content, user=user)
        post.save()
        return HttpResponseRedirect(reverse(index))
def profile_post(request,user_id):
    user=User.objects.get(pk=user_id)
    Following=Follow.objects.filter(user=user)
    allPosts=Post.objects.filter(user=user).order_by("id").reverse()
    Follower=Follow.objects.filter(user_follower=user)
    try:
        checkFollow=Follower.filter(user=User.objects.get(pk=request.user.id))
        if len(checkFollow)!=0:
            IsFollowing=True
        else:
            IsFollowing=False
    except:
        IsFollowing=False

    # use filter method for the post of particular user
    
    # pagination of django
    paginator=Paginator(allPosts,2)
    pgno=request.GET.get('page')
    post_page=paginator.get_page(pgno)
    return render(request, "network/profile.html",{
        "allPosts":allPosts,
        "post_page":post_page,
        "username":user.username,
        "follower":Follower,
        "following":Following,
        "isfollowing":IsFollowing,
        "user_profile":user
    })
def follow(request):
    userfollow=request.POST["userfollow"]
    currentUser=User.objects.get(pk=request.user.id)
    userfollowData=User.objects.get(username=userfollow)
    f=Follow(user=currentUser,user_follower=userfollowData)
    f.save()
    user_id=userfollowData.id
    return HttpResponseRedirect(reverse(profile_post,kwargs={'user_id':user_id}))
def unfollow(request):
    userfollow=request.POST["userfollow"]
    currentUser=User.objects.get(pk=request.user.id)
    userfollowData=User.objects.get(username=userfollow)
    f=Follow.objects.get(user=currentUser,user_follower=userfollowData)
    f.delete()
    user_id=userfollowData.id
    return HttpResponseRedirect(reverse(profile_post,kwargs={'user_id':user_id}))
def following(request):
    currentUser=User.objects.get(pk=request.user.id)
    followings=Follow.objects.filter(user=currentUser)
    allPosts=Post.objects.all().order_by('id').reverse()
    # to get the data of following users
    followingPosts=[]
    for post in allPosts:
        for person in followings:
            if person.user_follower==post.user:
                followingPosts.append(post)
    paginator=Paginator(followingPosts,2)
    pgno=request.GET.get('page')
    post_page=paginator.get_page(pgno)
    return render(request, "network/following.html",{
      "post_page":post_page
    })
def edit(request,post_id):
    if request.method=="POST":
        data=json.loads(request.body)
        edit_post=Post.objects.get(pk=post_id)
        edit_post.Content=data["content"]
        edit_post.save()
        return JsonResponse({
            "message":"Change Successful",
            "data":data["content"]
        })
        # both remove and add are like and unlike function 

def add(request,post_id):    
    post=Post.objects.get(pk=post_id)
    user=User.objects.get(pk=request.user.id)
    new=Like(user=user,post=post)
    new.save()
    return JsonResponse({
        "message":"Liked Successfully"
        })
def remove(request,post_id):
    post=Post.objects.get(pk=post_id)
    user=User.objects.get(pk=request.user.id)
    likess=Like.objects.filter(user=user,post=post)
    likess.delete()
    return JsonResponse({
        "message":"UnLiked Successfully"
        })