from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse

class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'Cooking Blog'
        context["blog_url"] = reverse('blog:post_list')
        return context
    
index = IndexView.as_view()