from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Xidmetler(models.Model):
    name = models.CharField(verbose_name='Xidmet adı', max_length=256, null=True, blank=True)
    iconimage = models.ImageField(verbose_name='Icon', null=True, blank=True)
    image = models.ImageField(verbose_name='Şəkil', null=True, blank=True)
    description = RichTextField(verbose_name='Haqqında Ətraflı Məlumat', blank=True, null=True)
   
    def __str__(self):
        return self.name


class XidmetlerAltKateqoriya(models.Model):
    name = models.CharField(verbose_name='Xidmet adı', max_length=256, null=True, blank=True)
    category = models.OneToOneField(Xidmetler,verbose_name='Kateqoriya',  related_name='projects',on_delete=models.CASCADE)
    iconimage = models.ImageField(verbose_name='Icon', null=True, blank=True)
    image = models.ImageField(verbose_name='Şəkil', null=True, blank=True)
    description = RichTextField(verbose_name='Haqqında Ətraflı Məlumat', blank=True, null=True)
   
    def __str__(self):
        return self.name

class Images(models.Model):
    xidmet = models.ForeignKey(Xidmetler, on_delete=models.CASCADE, related_name='sekiller')
    images = models.ImageField(verbose_name='Şəkil', null=True, blank=True)

    def __str__(self):
        return self.xidmet.name + ' şəkilləri'