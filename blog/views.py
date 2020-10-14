from django.shortcuts import render
from django.http import HttpResponse
from . models import Blogposts
# Create your views here.

def index(request):
    mypost = Blogposts.objects.all()

    return render(request, 'blog/index.html', {'mypost':mypost})

def blogpost(request, id):
    post = Blogposts.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html', {'post':post})