from django.shortcuts import render
from .models import Post
from django.http import Http404


def post_list(request):
  posts = Post.published.all()
  return render(request=request,
                template_name='blog/post/list.html',
                context={'posts': posts})


def post_detail(request, id):
  try:
    post = Post.published.get(id=id)
  except Post.DoesNotExist:
    raise Http404("No Post found.")
  return render(request=request,
                template_name='blog/post/detail.html',
                context={'post': post})
