from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return  self.title
class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category