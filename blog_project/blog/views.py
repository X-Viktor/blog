from django.views import generic

from .models import Blog, Post


class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/blog-list.html'


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post-list.html'

    def get_queryset(self):
        """Sort posts in reverse chronological order"""
        if not self.request.user.is_anonymous:
            return Post.objects.filter(blog__subscribers__in=[self.request.user]).order_by('-time')
        return []
