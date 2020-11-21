from django.urls import path

from .views import BlogListView, BlogDetailView, PostListView, PostDetailView, \
    BlogSubscribeView, BlogUnsubscribeView, PostDeleteView, PostMarkAsReadView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('feed/', PostListView.as_view(), name='post_list'),
    path('<int:pk>/subscribe/', BlogSubscribeView.as_view(), name='subscribe'),
    path('<int:pk>/unsubscribe/', BlogUnsubscribeView.as_view(), name='unsubscribe'),
    path('feed/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('feed/<int:pk>/confirm_delete/', PostDeleteView.as_view(), name='post_delete'),
    path('feed/<int:pk>/mark_as_read/', PostMarkAsReadView.as_view(), name='post_mark_as_read'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
]