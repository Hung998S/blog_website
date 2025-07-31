from django.shortcuts import render, redirect
from blogs.models import Category, Blogs
from .forms import RegistraionForm
# from django.contrib.auth import aauthenticate
from django.contrib import auth 
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    categories = Category.objects.all()
    featrued_post = Blogs.objects.filter(is_feacherd = True, status = 'published' )
    posts = Blogs.objects.filter(is_feacherd = False, status='published')
    
    context = {
        'categories':categories,
        'featured_post': featrued_post,
        'posts': posts
    }
    return render(request,'home.html', context)


# register
def register(request):
    if request.method=="POST":
        form = RegistraionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistraionForm()
    context={
        'form':form
    }
    return render(request, 'register.html', context)

# Login
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')