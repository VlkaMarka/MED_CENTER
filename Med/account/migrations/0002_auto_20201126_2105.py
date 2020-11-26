# Generated by Django 3.1.2 on 2020-11-26 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='diseases',
            field=models.ManyToManyField(blank='True', to='app.Disease', verbose_name='Заболевания'),
        ),
        migrations.AddField(
            model_name='account',
            name='positions_doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='account.positions', verbose_name='Должность'),
        ),
    ]