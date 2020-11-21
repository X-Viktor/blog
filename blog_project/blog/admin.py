from django.contrib import admin

from .models import Blog, Post, UsersReader


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    prepopulated_fields = {
        'slug': ('title', ),
    }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'time', 'blog']


@admin.register(UsersReader)
class UsersReaderAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']
