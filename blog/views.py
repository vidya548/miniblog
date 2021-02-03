from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Signform,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post
from  django.contrib.auth.models import Group
#home
def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

#About
def about(request):
    return render (request,'blog/about.html')

#Contact
def contact(request):
    return render (request,'blog/contact.html')

#Dashbord
def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        return render (request,'blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')


#signup
def signup(request):
    if request.method=='POST':
        form = Signform(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! you have become an Authour')
            form.save()
            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
            return HttpResponseRedirect('/signup/')
    else:
        form= Signform()
    return render (request,'blog/signup.html',{'form':form})

#login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Logged in successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=LoginForm()
        return render (request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

#user_logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                dec=form.cleaned_data['decription']
                pst=Post(title=title,decription=dec)
                pst.save()
                form=PostForm()
        else:
            form=PostForm()
        return render(request, 'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')