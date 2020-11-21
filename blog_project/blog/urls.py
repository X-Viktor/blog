from django.urls import path

from .views import BlogListView, PostListView, PostDetailView, \
    BlogSubscribeView, BlogUnsubscribeView, PostMarkAsReadView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/subscribe', BlogSubscribeView.as_view(), name='subscribe'),
    path('<int:pk>/unsubscribe', BlogUnsubscribeView.as_view(), name='unsubscribe'),
    path('posts/<int:pk>/mark_as_read', PostMarkAsReadView.as_view(), name='post_mark_as_read'),
]