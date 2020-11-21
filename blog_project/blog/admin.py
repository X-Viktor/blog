from django.contrib import admin

from .models import Blog, Post


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    prepopulated_fields = {
        'slug': ('title', ),
    }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'time', 'blog']
