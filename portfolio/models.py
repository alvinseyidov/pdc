from django.db import models
from xidmetler.models import Xidmetler
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name='Kateqoriya adı', max_length=256, null=True, blank=True)
   
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(verbose_name='Proyektin Adı', max_length=256,null=True, blank=True)
    category = models.ManyToManyField(Xidmetler,verbose_name='Kateqoriya',  related_name='portfolios')
    image = models.ImageField(verbose_name='Şəkil', null=True, blank=True)
    description = RichTextField(verbose_name='Haqqında Ətraflı Məlumat', blank=True, null=True)
    
    def __str__(self):
        return self.name