# blog > views.py

from django.shortcuts import render
from .models import Post, Tag
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, TagForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_deleted=False)
    
post_list = PostListView.as_view()

class PostDetailView(DetailView):
    model = Post
    
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return render(request, 'blog/404.html', status=404)
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.view_count += 1
        post.save()
        return super().get_object(queryset)
    
post_detail = PostDetailView.as_view()

class PostCreateview(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/form.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

post_write = PostCreateview.as_view()

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/form2.html'
    
    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def handle_no_permission(self): 
        if self.raise_exception or self.request.user.is_authenticated:
            return render(self.request, 'blog/403.html', status=403)
        return super().handle_no_permission()
    
post_edit = PostUpdateView.as_view()

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def handle_no_permission(self): 
        if self.raise_exception or self.request.user.is_authenticated:
            return render(self.request, 'blog/403.html', status=403)
        return super().handle_no_permission()

post_delete = PostDeleteView.as_view()

class SearchListView(ListView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(Q(title__contains=q) | Q(tag__name__contains=q)).distinct().order_by('-created_at').filter(is_deleted=False)
        return qs

post_search = SearchListView.as_view()