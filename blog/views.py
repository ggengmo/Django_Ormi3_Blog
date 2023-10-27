# blog > views.py

from django.shortcuts import render
from .models import Post, Tag, Search
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, TagForm
from django.urls import reverse_lazy
from django.db.models import Q

class PostListView(ListView):
    model = Post

post_list = PostListView.as_view()

class PostDetailView(DetailView):
    model = Post

post_detail = PostDetailView.as_view()

class PostCreateview(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/form.html'
    success_url = reverse_lazy('blog:post_list')

post_write = PostCreateview.as_view()

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/form2.html'
    
    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})
    
post_edit = PostUpdateView.as_view()

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

post_delete = PostDeleteView.as_view()

class SearchListView(ListView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

post_search = SearchListView.as_view()
