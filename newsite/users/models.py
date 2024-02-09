from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    surname = models.CharField(max_length=100, blank=True, null=True,
                               default=None, verbose_name='Отчество')
    data_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    diagnosis = models.TextField(blank=True, null=True, verbose_name='Диагноз')
    anamnesis = models.TextField(blank=True, null=True, verbose_name='Анамнез')
    allergy = models.CharField(max_length=250, blank=True, null=True, verbose_name='Аллергия')
    height = models.IntegerField(blank=True, null=True, verbose_name='Рост')
    weight = models.IntegerField(blank=True, null=True, verbose_name='Вес')

    class Meta():
        verbose_name = 'пациент'
        verbose_name_plural = 'пациенты'
        ordering = ['last_name', 'first_name', 'surname']


