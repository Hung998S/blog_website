from django.shortcuts import render
from blogs.models import Category, Blogs

def home(request):
    categories = Category.objects.all()
    featrued_post = Blogs.objects.filter(is_feacherd = True )
    # print(featrued_post)
    context = {
        'categories':categories,
        'featured_post': featrued_post
    }
    return render(request,'home.html', context)