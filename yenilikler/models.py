from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Yenilikler(models.Model):
    name = models.CharField(verbose_name='Proyektin Adı', max_length=256,null=True, blank=True)
    ikon = models.ImageField(verbose_name='Ikon', null=True, blank=True)
    image = models.ImageField(verbose_name='Şəkil', null=True, blank=True)
    description = RichTextField(verbose_name='Haqqında Ətraflı Məlumat', blank=True, null=True)
    
    def __str__(self):
        return self.name