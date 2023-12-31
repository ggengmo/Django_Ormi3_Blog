# blog > urls.py

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('write/', views.post_write, name='post_write'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('search/', views.post_search, name='post_search'),
    path('<int:pk>/comment_new/', views.comment_new, name='comment_new'),
    path('<int:post_pk>/comment/<int:pk>/edit', views.comment_edit, name='comment_edit'),
    path('<int:post_pk>/comment/<int:pk>/delete', views.comment_delete, name='comment_delete'),
]
