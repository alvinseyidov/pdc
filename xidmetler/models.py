from django.db import models
from ckeditor.fields import RichTextField

class Xidmetler(models.Model):
    name = models.CharField(verbose_name='Xidmət adı', max_length=256, null=True, blank=True)
    iconimage = models.ImageField(verbose_name='İkon', null=True, blank=True)
    image = models.ImageField(verbose_name='Şəkil', null=True, blank=True)
    short_description = models.CharField(max_length=512)
    description = RichTextField(verbose_name='Haqqında ətraflı məlumat', blank=True, null=True)

    class Meta:
        verbose_name = "Xidmət"
        verbose_name_plural = "Xidmətlər"

    def __str__(self):
        return self.name


class XidmetlerAltKateqoriya(models.Model):
    name = models.CharField(verbose_name='Xidmət adı', max_length=256, null=True, blank=True)
    category = models.OneToOneField(Xidmetler, verbose_name='Kateqoriya', related_name='projects', on_delete=models.CASCADE)
    iconimage = models.ImageField(verbose_name='İkon', null=True, blank=True)
    image = models.ImageField(verbose_name='Şəkil', null=True, blank=True)
    description = RichTextField(verbose_name='Haqqında ətraflı məlumat', blank=True, null=True)

    class Meta:
        verbose_name = "Xidmət Alt Kateqoriya"
        verbose_name_plural = "Xidmət Alt Kateqoriyalar"

    def __str__(self):
        return self.name


class Images(models.Model):
    xidmet = models.ForeignKey(Xidmetler, on_delete=models.CASCADE, related_name='sekiller', verbose_name='Xidmət')
    images = models.ImageField(verbose_name='Şəkil', null=True, blank=True)

    class Meta:
        verbose_name = "Xidmət Şəkli"
        verbose_name_plural = "Xidmət Şəkilləri"

    def __str__(self):
        return f"{self.xidmet.name} şəkilləri"
