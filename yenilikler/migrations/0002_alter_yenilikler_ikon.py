# Generated by Django 3.2 on 2021-05-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yenilikler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yenilikler',
            name='ikon',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Ikon'),
        ),
    ]
