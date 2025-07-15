from django.shortcuts import render, HttpResponse, get_object_or_404
import random
from posts.models import Post

def home(request):
    return render(request, "base.html")

def html_view(request):
    return render(request, 'base.html')

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', context={'posts': posts})

def post_detail(request):
    post = Post.objects.get(id = 1)
    return render(request, 'posts/post.html', context={"post": post})