from django.shortcuts import render, redirect
from blogs.models import Category, Blogs
from .forms import RegistraionForm

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