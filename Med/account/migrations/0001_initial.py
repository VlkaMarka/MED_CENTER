# Generated by Django 3.1.2 on 2020-11-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Логин')),
                ('surname_doctor', models.CharField(max_length=50, null=True, verbose_name='Фамилия врача')),
                ('name_doctor', models.CharField(max_length=50, null=True, verbose_name='Имя врача')),
                ('middlename_doctor', models.CharField(max_length=50, null=True, verbose_name='Отчество врача')),
                ('date_joined', models.DateTimeField(auto_now_add=True, max_length=50, null=True, verbose_name='Дата регистраци')),
                ('last_login', models.DateTimeField(auto_now=True, max_length=50, null=True, verbose_name='Дата последнего входа')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Доктор-администратор')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Аккаунт',
                'verbose_name_plural': 'Аккаунты',
            },
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positions_name', models.CharField(max_length=50, verbose_name='Наименование роли')),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
            },
        ),
    ]
