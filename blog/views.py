# blog > views.py

from typing import Any
from django.shortcuts import render, redirect
from .models import Post, Tag, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, TagForm, CommentForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator

class PostListView(ListView):
    model = Post
    paginate_by = 4

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_deleted=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()  # 태그 리스트를 컨텍스트에 추가합니다.
        return context
    
post_list = PostListView.as_view()

class PostDetailView(DetailView):
    model = Post
    
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return render(request, 'blog/404.html', status=404)
    
    def get_object(self, queryset=None):
        try:
            pk = self.kwargs.get('pk')
            post = Post.objects.get(pk=pk)
            post.view_count += 1
            post.save()
        except Post.DoesNotExist:
            return render(self.request, 'blog/404.html', status=404)
        return super().get_object(queryset)
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', pk=self.get_object().pk)
        else:
            return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_comments'] = self.object.comments.filter(nested_reply__isnull=True).order_by('-created_at')
        context['comment_form'] = CommentForm()
        context['tags'] = Tag.objects.all()
        return context
    
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
    paginate_by = 4

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(Q(title__contains=q) | Q(tag__name__contains=q)).distinct().order_by('-created_at').filter(is_deleted=False)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

post_search = SearchListView.as_view()

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        form.instance.nested_reply_id = self.request.POST.get('nested_reply')
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()

comment_new = CommentCreateView.as_view()

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/form3.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk':self.object.post.pk})
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    def handle_no_permission(self): 
        if self.raise_exception or self.request.user.is_authenticated:
            return render(self.request, 'blog/403.html', status=403)
        return super().handle_no_permission()
    
    def form_valid(self, form):
        form.instance.nested_reply_id = self.request.POST.get('nested_reply')
        return super().form_valid(form)
    
comment_edit = CommentUpdateView.as_view()

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk':self.object.post.pk})
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    def handle_no_permission(self): 
        if self.raise_exception or self.request.user.is_authenticated:
            return render(self.request, 'blog/403.html', status=403)
        return super().handle_no_permission()

comment_delete = CommentDeleteView.as_view()