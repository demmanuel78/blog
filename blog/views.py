from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from blog.forms import CForm, RForm, TForm
from .models import Category, Comment, User, Post
import datetime
from django.contrib.auth import login, authenticate, logout



# Create your views here.

def index(request):
    posts = Post.objects.all().order_by("-date")
    count = posts.count()
    categories = Category.objects.all()
    date = datetime.datetime.now()
    data = {
        "date": date,
        "posts": posts,
        "count": count,
        "categories": categories 

        }
    return render(request, "blog/index.html", data)


def register(request):
    form = RForm()

    if request.method =="POST":
        form = RForm(request.POST)

        if form.is_valid:
            form.save()
            messages.success(request,"Registration Success")
            
            return redirect("register")
    
    date = datetime.datetime.now()

    data = {
        "date": date,
        "form": form
    }        

    return render(request, "blog/register.html", data)


def createpost(request, id):
    if not request.user.is_authenticated:
       return redirect("login")
    form = TForm()
    
    if request.method == "POST":
        form = TForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.user_id = request.user.id
            post.category_id = id
            post.save()
            messages.success(request, "Post Uploaded Successfully")
            return  redirect("createpost", id=id)

    data = {
        "form": form,
        "categoryid": id        
    }
    return render(request, "blog/createpost.html", data)


def postcategory(request, id):
    posts = Post.objects.filter(category=id).order_by("-id")
    categories = Category.objects.all().order_by("-id")
    count = posts.count()
    date = datetime.datetime.now()
    
    data = {
        "posts": posts,
        "category": posts[0].category,
        "categories": categories,
        "count": count,
        "date": date,
        "categoryid":id
        
    }
    return render(request, "blog/postcategory.html", data)

def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=id)
    count = comments.count()
    date = datetime.datetime.now()
     
    form = CForm()
    if request.method == "POST":
        form = CForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post_id= post.id
            comment.user_id = request.user.id
            comment.save()
            messages.success(request, "Comment Uploaded Successfully")
            return  redirect("post_details", id=post.id)

    data={
        "post": post,
        "comments" :comments,
        "count": count,
        "form": form,
        "date": date,
               
    }
    return render(request, "blog/post_details.html", data)



def recentpost(request):
    posts = Post.objects.all().order_by("-id")[:3]
    categories = Category.objects.all()
    count = posts.count()
    categories = Category.objects.all()
    date = datetime.datetime.now()

    data = {
        "date": date,
        "posts": posts,
        "count": count,
        "categories": categories 

    }
    return render(request, "blog/index.html", data) 


def userpost(request, id):
    posts = Post.objects.filter(user=id).order_by("-date")
    count = posts.count()
    categories = Category.objects.all()
    date = datetime.datetime.now()
    data = {
        "date": date,
        "posts": posts,
        "count": count,
        "categories": categories,
    }
    return render(request, "blog/index.html", data)


def search(request):    
    if request.method == "GET":
       search = request.GET.get("searchvalue")
       posts = Post.objects.filter(title__icontains=search).order_by("title")
       
       count = posts.count()
       categories = Category.objects.all()
       date = datetime.datetime.now()
    data ={
        "date": date,
        "posts": posts,
        "count": count,
        "categories": categories,
        "searchvalue": search
    }
    return render(request, "blog/index.html", data)
    


def updateprofile(request, id):
    userdetails = get_object_or_404(User, id=id)    
    
    form = RForm(instance=userdetails)
    if request.method == "POST":
        form = RForm(request.POST, instance=userdetails)
        if form.is_valid:
            form.save()
            messages.success(request, "Update successfully done")
            return redirect("updateprofile", id=userdetails.id)

    data = {
        "form": form,
        
    }
    return render(request, "blog/updateprofile.html", data)


