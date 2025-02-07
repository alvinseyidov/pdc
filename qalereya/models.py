from django.db import models

class Gallery(models.Model):
    image = models.ImageField(verbose_name='Qalereya şəkli', null=True, blank=True)

    class Meta:
        verbose_name = "Qalereya"
        verbose_name_plural = "Qalereya şəkilləri"

    def __str__(self):
        return f"Qalereya Şəkil {self.id}"
