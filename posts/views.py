from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
import random
from posts.models import Post
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "base.html")

def html_view(request):
    return render(request, 'base.html')

@login_required(login_url="/login")
def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', context={'posts': posts})

@login_required(login_url="/login")
def post_detail_view(request, post_id):
    post = Post.objects.filter(id = post_id).first()
    return render(request, 'posts/post_detail.html', context = {'post': post})

@login_required(login_url="/login")
def post_create_view(request):
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save()
                return redirect(f'/posts/{post.id}')
        else:
            form = PostForm()
    
        return render(request, 'posts/post_create.html', {'form': form})


# def post_create_view(request):
#     if request.method == 'GET':
#         form = PostForm()
#         return render(request, 'posts/post_create.html', context={"form":form})
    
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if not form.is_valid():
#             return render(request, 'posts/post_create.html', context={"form":form})

#         title = form.cleaned_data.get("title")
#         content = form.cleaned_data.get("content")
#         image = form.cleaned_data.get("image")
#         post = Post.objects.create(title = title, content = content, image = image)
#         return redirect(f'/posts/{post.id}')



    