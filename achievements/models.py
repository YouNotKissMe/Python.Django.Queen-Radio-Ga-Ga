from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator

import datetime
from datetime import date as datenow

choices_type = [('Учебно-организационное направление', 'Учебно-организационное направление'),
                ('Научно-методическое направление', 'Научно-методическое направление'),
                ('Организационно-воспитательное направление', 'Организационно-воспитательное направление')]


def MAX(choices):
    max = None
    for i in choices:
        if max:
            if max < len(i[0]):
                max = len(i[0])
        else:
            max = len(i[0])
    return max


class Achievements(models.Model):
    choice = [('Свидетельство', 'Свидетельство'),
              ('Сертификат', 'Сертификат'),
              ('Благодарность', 'Благодарность'),
              ('Награда', 'Награда'),
              ('Ученая степень', 'Ученая степень'),
              ('Ученое звание', 'Ученое звание')]
    key = models.ForeignKey(User, on_delete=models.CASCADE)
    choice_length = MAX(choice)
    achievements_type = models.CharField(max_length=choice_length, choices=choice, verbose_name='Тип',
                                         default='Ученое звание')
    name = models.CharField(max_length=200, verbose_name='Наименование')
    date_of_receiving = models.DateField(verbose_name='Дата получения',
                                         validators=[MaxValueValidator(limit_value=datenow(datetime.datetime.now().year,
                                                                                           datetime.datetime.now().month,
                                                                                           datetime.datetime.now().day))],
                                         help_text='Формат дд.мм.гггг')
    file = models.FileField(verbose_name='Фаил',
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'docx', 'doc', 'pdf'])])
    the_direction_of_self_development = models.TextField(choices=choices_type,
                                                         verbose_name='Направление саморазвития',
                                                         default=choices_type[0][0])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Достижения'
        verbose_name_plural = 'Достижения'


class Education(models.Model):
    key = models.ForeignKey(User, on_delete=models.CASCADE)
    choices = [
        ('незаконченное высшее', 'незаконченное высшее'),
        ('среднее', 'среднее'),
        ('среднее профессиональное', 'среднее профессиональное'),
        ('среднее специальное', 'среднее специальное'),
        ('профессиональная переподготовка', 'профессиональная переподготовка'),
        ('высшее', (
            ('специалитет', 'специалитет'),
            ('бакалавриат', 'бакалавриат'),
            ('магистратура', 'магистратура'),
            ('аспирантура', 'аспирантура'),
            ('кандидат наук', 'кандидат наук'),
            ('доктор наук', 'доктор наук')
        ))]
    level = models.TextField(choices=choices, verbose_name='Уровень', default=choices[0][0])
    faculty = models.CharField(max_length=100, verbose_name='Факульет')
    specialization = models.CharField(verbose_name='Специализация', max_length=100)
    educational_organization = models.CharField(verbose_name='Образовательная организация', max_length=100)
    date = models.DateField(verbose_name='Дата Окончания',
                            validators=[MaxValueValidator(limit_value=datenow(datetime.datetime.now().year,
                                                                              datetime.datetime.now().month,
                                                                              datetime.datetime.now().day))
                                        ])

    def __str__(self):
        return self.key.first_name + ' ' + self.key.last_name

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'


class ProfessionalDevelopment(models.Model):
    key = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата Окончания',
                            validators=[MaxValueValidator(limit_value=datenow(datetime.datetime.now().year,
                                                                              datetime.datetime.now().month,
                                                                              datetime.datetime.now().day))
                                        ])
    educational_organization = models.CharField(verbose_name='Образовательная организация', max_length=100)
    name_theme = models.CharField(verbose_name='Наименование программы/темы', max_length=100)
    duration_of_training = models.PositiveSmallIntegerField(verbose_name='Срок обучения(мес.)', validators=[
        MinValueValidator(limit_value=0
                          )])
    number_of_hours = models.PositiveSmallIntegerField(verbose_name='Количество часов',
                                                       validators=[
                                                           MinValueValidator(limit_value=10
                                                                             )]
                                                       )
    number_document = models.PositiveSmallIntegerField(verbose_name='№ документа', unique=True)
    the_direction_of_self_development = models.TextField(choices=choices_type,
                                                         verbose_name='Направление саморазвития',
                                                         default=choices_type[0][0])

    def __str__(self):
        return self.name_theme

    class Meta:
        verbose_name = 'Повышение квалификации'
        verbose_name_plural = 'Повышение квалификации'
