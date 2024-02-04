from django.db import models
from django.contrib.auth import get_user_model

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):

    PERIODICITY_CHOICES = [
        (1, 'Каждые понедельник, среда, пятница'),
        (2, 'Каждые вторник, четверг, суббота'),
        (3, 'Каждый будний день'),
        (4, 'Каждые выходные')
    ]

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
        related_name='creator', verbose_name='пользователь')
    place = models.CharField(max_length=255, verbose_name='место выполнения')
    time = models.TimeField(verbose_name='время, когда выполняется привычка')
    action = models.CharField(max_length=255, verbose_name='действие')
    is_pleasure = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey(
        'self', on_delete=models.SET_NULL, **NULLABLE,
        related_name='main_habit', verbose_name='связанная привычка')
    periodicity = models.PositiveIntegerField(default=1, choices=PERIODICITY_CHOICES, verbose_name='периодичность')
    reward = models.CharField(max_length=255, **NULLABLE, verbose_name='вознаграждение')
    duration = models.DurationField(verbose_name='длительность выполнения')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')
    objects = models.Manager()

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('pk',)