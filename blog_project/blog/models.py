from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
