# Generated by Django 4.0.4 on 2022-05-05 05:28

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_alter_profile_birth_date_alter_profile_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2004, 5, 5))], verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2022, 5, 5))], verbose_name='Дата начала трудовой деятельности'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.TextField(blank=True, choices=[('Директор', 'Директор'), ('Заместитель директора', 'Заместитель директора'), ('Заведующий отделением', 'Заведующий отделением'), ('Заведующий методическим кабинетом', 'Заведующий методическим кабинетом'), ('Методист', 'Методист'), ('Председатель предметно-цикловой комиссией', 'Председатель предметно-цикловой комиссией'), ('Преподаватель', 'Преподаватель'), ('Мастер производственного обучения', 'Мастер производственного обучения')], default='Директор', null=True, verbose_name='Должность'),
        ),
    ]