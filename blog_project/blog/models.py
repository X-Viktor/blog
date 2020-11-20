from django.db import models


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


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
