from django import forms
from .models import Post, Tag, Search

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'main_image', 'file_upload']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']