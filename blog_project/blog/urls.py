from django.urls import path

from .views import BlogListView, PostListView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('posts/', PostListView.as_view(), name='post_list'),
]