from django.db import models

# Create your models here.

class Xidmetler(models.Model):
    name = models.CharField(verbose_name='Xidmet adı', max_length=256, null=True, blank=True)
   
    def __str__(self):
        return self.name