from django.db import models
from ckeditor.fields import RichTextField

class Yenilikler(models.Model):
    title = models.CharField(verbose_name="Başlıq", max_length=255)
    author = models.CharField(verbose_name="Müəllif", max_length=255, null=True, blank=True)
    image = models.ImageField(verbose_name="Şəkil", upload_to="news_images/", null=True, blank=True)
    content = RichTextField(verbose_name="Məqalə Mətni", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="Tarix", auto_now_add=True)

    class Meta:
        verbose_name = "Yenilik"
        verbose_name_plural = "Yeniliklər"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
