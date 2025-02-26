from django.db import models
from xidmetler.models import Xidmetler
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(verbose_name='Kateqoriya adı', max_length=256, null=True, blank=True)

    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(verbose_name='Proyektin adı', max_length=256, null=True, blank=True)
    customer = models.CharField(verbose_name='Müştəri adı', max_length=256, null=True, blank=True)
    address = models.CharField(verbose_name='Proyektin ünvanı', max_length=256, null=True, blank=True)
    teslim = models.CharField(verbose_name='Təslim tarixi və ya davam edir', max_length=256, null=True, blank=True)
    category = models.ManyToManyField(Xidmetler, verbose_name='Xidmət kateqoriyası', related_name='portfolios')
    image = models.ImageField(verbose_name='Proyekt şəkli', null=True, blank=True)
    description = RichTextField(verbose_name='Proyekt haqqında ətraflı məlumat', blank=True, null=True)

    class Meta:
        verbose_name = "Proyekt"
        verbose_name_plural = "Proyektlər"

    def __str__(self):
        return self.name


class Images(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='sekiller', verbose_name='Proyekt')
    images = models.ImageField(verbose_name='Proyekt şəkli', null=True, blank=True)

    class Meta:
        verbose_name = "Proyekt Şəkli"
        verbose_name_plural = "Proyekt Şəkilləri"

    def __str__(self):
        return f"{self.project.name} şəkilləri"
