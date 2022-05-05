from django.db import models
from django.contrib.auth.models import User
from django.core.validators import ValidationError


class Picture(models.Model):
    lvl_one = models.SmallIntegerField('Репродуктивно-адаптивный уровень', default=1)
    lvl_two = models.SmallIntegerField('Активно-поисковый уровень', default=2)
    lvl_three = models.SmallIntegerField('Интенсивно-творческий уровень', default=3)

    def save(self, *args, **kwargs):
        if not self.pk and Picture.objects.exists():
            raise ValidationError('Может быть только 1 объект модели, в нем вы должны изменять значения')
        return super(Picture, self).save(*args, **kwargs)

    def __str__(self):
        return 'Уровни педагогического саморазвития преподавателя'

    class Meta:
        verbose_name = 'Редактирование планок уровня саморазвития преподавателя'
        verbose_name_plural = 'Редактирование планок уровня саморазвития преподавателя'
