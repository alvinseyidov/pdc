from django.db import models
from ckeditor.fields import RichTextField



class KorporativXidmetler(models.Model):
    name = models.CharField(verbose_name='Xidmət adı', max_length=256, null=True, blank=True)
    image = models.ImageField(verbose_name='Şəkil', null=True, blank=True)
    short_description = models.CharField(max_length=512)
    description = RichTextField(verbose_name='Haqqında ətraflı məlumat', blank=True, null=True)
    icon1 = models.FileField()
    icon2 = models.FileField()

    class Meta:
        verbose_name = "Korporativ Xidmət"
        verbose_name_plural = "Korporativ Xidmətlər"

    def __str__(self):
        return self.name

class Xidmetler(models.Model):
    name = models.CharField(verbose_name='Xidmət adı', max_length=256, null=True, blank=True)
    image = models.ImageField(verbose_name='Şəkil', null=True, blank=True)
    short_description = models.CharField(max_length=512)
    description = RichTextField(verbose_name='Haqqında ətraflı məlumat', blank=True, null=True)
    icon1 = models.FileField()
    icon2 = models.FileField()

    class Meta:
        verbose_name = "Xidmət"
        verbose_name_plural = "Xidmətlər"

    def __str__(self):
        return self.name


class XidmetlerAltKateqoriya(models.Model):
    name = models.CharField(verbose_name='Xidmət adı', max_length=256, null=True, blank=True)
    category = models.ForeignKey(Xidmetler, verbose_name='Kateqoriya', related_name='sub_categories', on_delete=models.CASCADE)
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


class KorporativImages(models.Model):
    xidmet = models.ForeignKey(KorporativXidmetler, on_delete=models.CASCADE, related_name='sekiller', verbose_name='Xidmət')
    images = models.ImageField(verbose_name='Şəkil', null=True, blank=True)

    class Meta:
        verbose_name = "Xidmət Şəkli"
        verbose_name_plural = "Xidmət Şəkilləri"

    def __str__(self):
        return f"{self.xidmet.name} şəkilləri"