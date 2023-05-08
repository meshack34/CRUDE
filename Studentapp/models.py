from django.db import models
from django.urls import reverse 

# Create your models here.
from django.db import models
class Post(models.Model):
    name = models.CharField(max_length=200, null=True)
    maths = models.CharField(max_length=200, null=True)
    eng = models.CharField(max_length=200, null=True)
    kis = models.CharField(max_length=200, null=True)
    cre = models.CharField(max_length=200, null=True)
    science = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self): 
        return reverse('post_detail', args=[str(self.id)])