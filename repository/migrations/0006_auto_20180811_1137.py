# Generated by Django 2.0.7 on 2018-08-11 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_auto_20180808_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='theme',
            field=models.CharField(max_length=8, verbose_name='博客主题'),
        ),
    ]
