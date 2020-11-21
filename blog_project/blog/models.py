from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from .tasks import email_notification


class Blog(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    subscribers = models.ManyToManyField(
        'auth.User',
        related_name='subscribers',
        blank=True,
    )
    author = models.ForeignKey(
        'auth.User',
        related_name='blog',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class UsersRead(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        'blog.Post',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(
        Blog,
        related_name='post',
        on_delete=models.CASCADE
    )
    users_read = models.ManyToManyField(
        'auth.User',
        through=UsersRead,
        through_fields=('post', 'user'),
        blank=True
    )

    def __str__(self):
        return self.title


@receiver(post_save, sender=Post)
def post_created(sender, instance, created, **kwargs):
    if created:
        blog_title = instance.title
        url = f'http://localhost:8000/feed/{instance.pk}'
        user_emails = instance.blog.subscribers.values_list('email', flat=True)
        for email in user_emails:
            email_notification(email, blog_title, url)
