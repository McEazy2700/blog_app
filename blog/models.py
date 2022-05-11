from django.db import models
from user.models import CustomUser
from tag.models import Tag

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=160)
    content = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(
        upload_to='uploads/images/blog/', blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    tag_item = models.ManyToManyField(Tag, related_name='tags', null=True)

    def __str__(self):
        return self.title

