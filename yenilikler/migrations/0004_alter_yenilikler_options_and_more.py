# Generated by Django 5.1.5 on 2025-02-07 13:03

import ckeditor.fields
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yenilikler', '0003_alter_yenilikler_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='yenilikler',
            options={'ordering': ['-created_at'], 'verbose_name': 'Yenilik', 'verbose_name_plural': 'Yeniliklər'},
        ),
        migrations.RemoveField(
            model_name='yenilikler',
            name='description',
        ),
        migrations.RemoveField(
            model_name='yenilikler',
            name='ikon',
        ),
        migrations.RemoveField(
            model_name='yenilikler',
            name='name',
        ),
        migrations.AddField(
            model_name='yenilikler',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Müəllif'),
        ),
        migrations.AddField(
            model_name='yenilikler',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Məqalə Mətni'),
        ),
        migrations.AddField(
            model_name='yenilikler',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Tarix'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yenilikler',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Başlıq'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='yenilikler',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images/', verbose_name='Şəkil'),
        ),
    ]
