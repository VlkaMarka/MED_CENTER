# Generated by Django 3.1.2 on 2020-11-20 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201120_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='birthday_patient',
            field=models.DateField(max_length=50, verbose_name='День рождение пациента'),
        ),
    ]
