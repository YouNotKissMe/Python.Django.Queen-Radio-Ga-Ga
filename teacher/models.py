from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, ValidationError
from phonenumber_field.modelfields import PhoneNumberField
import datetime
from datetime import date as datenow


class Profile(models.Model):
    situation = [('Директор', 'Директор'),
                 ('Заместитель директора', 'Заместитель директора'),
                 ('Заведующий отделением', 'Заведующий отделением'),
                 ('Заведующий методическим кабинетом', 'Заведующий методическим кабинетом'),
                 ('Методист', 'Методист'),
                 ('Председатель предметно-цикловой комиссией', 'Председатель предметно-цикловой комиссией'),
                 ('Преподаватель', 'Преподаватель'),
                 ('Мастер производственного обучения', 'Мастер производственного обучения')]
    gender = [('Муж', 'Муж'), ('Жен', 'Жен')]
    key = models.OneToOneField(User, on_delete=models.CASCADE)
    gender_model = models.TextField(choices=gender, verbose_name='пол', blank=True, null=True,
                                    default=gender[0][0])
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество', blank=True, null=True)
    date = models.DateField(verbose_name='Дата начала трудовой деятельности', blank=True, null=True,

                            validators=[MaxValueValidator(limit_value=datenow(datetime.datetime.now().year,
                                                                              datetime.datetime.now().month,
                                                                              datetime.datetime.now().day))

                                        ])
    birth_date = models.DateField(verbose_name='Дата рождения', blank=True, null=True,
                                  validators=[MaxValueValidator(
                                      limit_value=datenow((datetime.datetime.now().year - 18),
                                                          datetime.datetime.now().month,
                                                          datetime.datetime.now().day))])
    job = models.TextField(verbose_name='Должность', choices=situation, blank=True, null=True,
                           default=situation[0][0])
    work_place = models.CharField(max_length=100, verbose_name='Место работы(филиал)', blank=True, null=True)
    telephone = PhoneNumberField(verbose_name='Телефон', help_text='введите номер в формате +7', blank=True, null=True)

    def clean(self):
        if self.birth_date.year + 18 > self.date.year:
            raise ValidationError(
                'по Законодательству РФ ,'
                'вы могли начать заниматься Преподавательской деятельностью только после совершеннолетия')

    def save(self, *args, **kwargs):
        # you can have regular model instance saves use this as well
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'
