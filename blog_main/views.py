from django.shortcuts import render
from blogs.models import Category, Blogs

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