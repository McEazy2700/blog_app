from django.db import models
from user .models import CustomUser

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=160)
    content = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(
        upload_to='uploads/images/blog/', blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    tag_item = models.ManyToManyField(Blog, related_name='tags')

    def __str__(self):
        return self.tag_name
