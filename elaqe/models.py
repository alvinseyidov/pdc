from django.db import models

class Contact(models.Model):
    full_name = models.CharField(verbose_name='Ad və Soyad', max_length=255)
    email = models.EmailField(verbose_name='E-poçt', max_length=255)
    phone = models.CharField(verbose_name='Telefon', max_length=20, null=True, blank=True)
    message = models.TextField(verbose_name='Mesaj')
    created_at = models.DateTimeField(verbose_name='Göndərilmə tarixi', auto_now_add=True)

    class Meta:
        verbose_name = "Əlaqə mesajı"
        verbose_name_plural = "Əlaqə mesajları"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.email}"
