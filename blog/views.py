# blog > views.py

from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

class PostListView(ListView):
    model = Post

post_list = PostListView.as_view()

class PostDetailView(DetailView):
    model = Post

post_detail = PostDetailView.as_view()