# Generated by Django 5.1.5 on 2025-02-26 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_category_options_alter_images_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='address',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Proyektin ünvanı'),
        ),
        migrations.AddField(
            model_name='project',
            name='customer',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Müştəri adı'),
        ),
        migrations.AddField(
            model_name='project',
            name='teslim',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Təslim tarixi və ya davam edir'),
        ),
    ]
