from django.db import models
from ckeditor.fields import RichTextField

class Gallery(models.Model):
    image = models.ImageField(verbose_name='Qalereya şəkli', null=True, blank=True)

    class Meta:
        verbose_name = "Qalereya"
        verbose_name_plural = "Qalereya"

    def __str__(self):
        return f"Qalereya Şəkil {self.id}"


class Partnyorlar(models.Model):
    image = models.ImageField(verbose_name='Partnyor loqosu', null=True, blank=True)

    class Meta:
        verbose_name = "Partnyor"
        verbose_name_plural = "Partnyorlar"

    def __str__(self):
        return f"Partnyor {self.id}"


class FAQ(models.Model):
    question = models.CharField(verbose_name='Sual', max_length=1000, null=True, blank=True)
    answer = models.CharField(verbose_name='Cavab', max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = "Tez-tez verilən sual"
        verbose_name_plural = "Tez-tez verilən suallar"

    def __str__(self):
        return self.question


class About(models.Model):
    description = RichTextField(verbose_name='Haqqımızda ətraflı məlumat', blank=True, null=True)

    class Meta:
        verbose_name = "Haqqımızda"
        verbose_name_plural = "Haqqımızda"

    def __str__(self):
        return "Haqqımızda Məlumat"


class Hashtag(models.Model):
    tag = models.CharField(verbose_name='Haştaq', max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = "Haştaq"
        verbose_name_plural = "Haştaqlar"

    def __str__(self):
        return self.tag
