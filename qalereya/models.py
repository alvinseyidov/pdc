from django.db import models

# Create your models here.

class Gallery(models.Model):
    image = models.ImageField(verbose_name='Şəkil', null=True, blank=True)
    
    