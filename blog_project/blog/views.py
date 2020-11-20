from django.shortcuts import render
from django.views import generic

from .models import Blog, Post


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog/blog-list.html'


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post-list.html'
