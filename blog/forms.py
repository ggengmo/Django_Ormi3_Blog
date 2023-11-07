from django import forms
from .models import Post, Tag, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'main_image', 'file_upload', 'tag']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'nested_reply']
        widgets = {
            'nested_reply': forms.HiddenInput(),
        }

