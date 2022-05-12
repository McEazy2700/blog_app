from django.db import models
from tinymce.models import HTMLField
from accounts.models import CustomUser
# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=160)
    content = HTMLField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title