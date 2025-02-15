from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'posts'
url_pattern = [
    path('',PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name= 'post_detail'),
]