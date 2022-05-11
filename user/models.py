from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/images/users/', blank=True, null=True)

    def __str__(self):
        return self.user.username