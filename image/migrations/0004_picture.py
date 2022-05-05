# Generated by Django 4.0.4 on 2022-05-05 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_alter_images_apy_alter_images_ity_alter_images_ray'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lvl_one', models.SmallIntegerField(default=1, verbose_name='Репродуктивно-адаптивный уровень')),
                ('lvl_two', models.SmallIntegerField(default=2, verbose_name='Активно-поисковый уровень')),
                ('lvl_three', models.SmallIntegerField(default=3, verbose_name='Интенсивно-творческий уровень')),
            ],
        ),
    ]
