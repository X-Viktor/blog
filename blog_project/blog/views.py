from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Blog, Post, UsersRead
from .forms import PostCreateForm


class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/blog-list.html'


class BlogDetailView(generic.DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/blog-detail.html'

    def get_object(self, queryset=None):
        """ Return posts belonging to a specific blog """
        super(BlogDetailView, self).get_object(queryset)
        return Post.objects.filter(blog__slug=self.kwargs['slug'])


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post-list.html'

    def get_queryset(self):
        """ Sort posts in reverse chronological order """
        if not self.request.user.is_anonymous:
            return Post.objects.filter(blog__subscribers__in=[self.request.user]).order_by('-time')
        return []


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post-detail.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'blog/confirm-delete.html'

    def get_object(self, queryset=None):
        """ Check to ensure post is owned by request.user """
        author = super(PostDeleteView, self).get_object()
        if not author.blog.author == self.request.user:
            raise Http404
        return author


class PostCreateView(generic.CreateView):
    form_class = PostCreateForm
    template_name = 'blog/post-create.html'

    def post(self, request, *args, **kwargs):
        """ Checking fields, user and blog availability """
        form = self.form_class(request.POST)
        if form.is_valid():
            if self.request.user.is_anonymous:
                not_registered = 'You must register or login'
                return render(request, self.template_name, {'form': form, 'not_registered': not_registered})
            blog = Blog.objects.get(author=self.request.user)
            if blog:
                post = form.save(commit=False)
                post.blog = blog
                post.save()
                return HttpResponseRedirect(reverse_lazy('post_detail', args=[post.pk]))
            no_blog = 'You must create a blog'
            return render(request, self.template_name, {'form': form, 'no_blog': no_blog})
        return render(request, self.template_name, {'form': form})


class BlogSubscribeView(generic.CreateView):
    def post(self, request, *args, **kwargs):
        """ Adding a user to the number of subscribers """
        blog = get_object_or_404(Blog, pk=kwargs.get('pk'))
        user = request.user
        if not blog.subscribers.filter(pk=user.pk).exists():
            blog.subscribers.add(user)
            return HttpResponse(f'User {user} subscribed')
        return HttpResponse(f'User {user} already subscribed.')


class BlogUnsubscribeView(generic.CreateView):
    def post(self, request, *args, **kwargs):
        """ Removing a user from the number of subscribers """
        blog = get_object_or_404(Blog, pk=kwargs.get('pk'))
        user = request.user
        if blog.subscribers.filter(pk=user.pk).exists():
            blog.subscribers.remove(user)
            readers = blog.post.values_list('users_read', flat=True)
            UsersRead.objects.filter(user__in=readers).delete()
            return HttpResponse(f'User {user} unsubscribed')
        return HttpResponse(f'User {user} already unsubscribed')


class PostMarkAsReadView(generic.CreateView):
    def post(self, request, *args, **kwargs):
        """ Mark a post as read """
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        user = request.user
        if not post.users_read.filter(pk=user.pk).exists():
            post.users_read.add(user)
            return HttpResponse(f'The post is marked as read for the user {user}')
        return HttpResponse(f'The post has already been marked as read for the user {user}')
