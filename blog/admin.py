from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Blog
# Register your models here.
class BlogAdmin(ModelAdmin):
    list_display = ['author', 'title']
admin.site.register(Blog, BlogAdmin)