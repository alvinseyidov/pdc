# Generated by Django 3.2 on 2021-05-22 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sekiller', to='portfolio.project'),
        ),
    ]