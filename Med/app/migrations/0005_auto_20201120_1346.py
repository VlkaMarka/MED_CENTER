# Generated by Django 3.1.2 on 2020-11-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201120_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='symptoms',
        ),
        migrations.AddField(
            model_name='patient',
            name='symptoms_patient',
            field=models.ManyToManyField(blank=True, related_name='symptoms_patient', to='app.Symptom', verbose_name='Симптомы'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birthday_patient',
            field=models.DateField(blank=True, max_length=50, null=True, verbose_name='День рождение пациента'),
        ),
    ]
