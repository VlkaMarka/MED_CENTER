# Generated by Django 3.1.2 on 2020-11-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='report',
            name='problem_description',
            field=models.TextField(max_length=50, verbose_name='Описание проблемы'),
        ),
    ]