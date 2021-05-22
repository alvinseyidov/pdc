from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Gallery(models.Model):
    image = models.ImageField(verbose_name='Şəkil', null=True, blank=True)
    
class Partnyorlar(models.Model):
    image = models.ImageField(verbose_name='Şəkil', null=True, blank=True)
 
class FAQ(models.Model):
    question = models.CharField(verbose_name='Sual', max_length=1000, null=True, blank=True)
    answer = models.CharField(verbose_name='Cavab', max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.question
    
class About(models.Model):
    description = RichTextField(verbose_name='Haqqında Ətraflı Məlumat', blank=True, null=True)

    def __str__(self):
        return self.question 

class Hashtag(models.Model):
    tag = models.CharField(verbose_name='Tag', max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.tag         