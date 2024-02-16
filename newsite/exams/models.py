from django.contrib import auth
from django.db import models


class Exam(models.Model):
    name = models.ForeignKey(
        'NameOfExam',
        on_delete=models.PROTECT,
        null=True,
        related_name='exam_name',
        verbose_name='Название исследования' # заменяет name в формах, Админ-панели, все будет в upper
    )
    data = models.DateField(verbose_name='Дата исследования')
    content = models.TextField(verbose_name='Заключение')
    patient = models.ForeignKey(auth.get_user_model(),
                                on_delete=models.CASCADE, verbose_name='Пациент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None,
                              blank=True, null=True, verbose_name='Фото исследования')
    confirmed = models.BooleanField(default=False, verbose_name='подтверждено')

    def str(self):
        return self.name

    class Meta():
        verbose_name = 'Обследование'  # используется в Админ-панели
        verbose_name_plural = 'Обследования'  # используется в Админ-панели
        ordering = ['data']


class NameOfExam(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название исследования')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Название исследования'
        verbose_name_plural = 'Названия исследований'
        ordering = ['name']


class Analysis(models.Model):
    name = models.ForeignKey('NameOfAnalysis',
                             on_delete=models.PROTECT,
                             related_name='analysis_name',
                             verbose_name='Название анализа')
    data = models.DateField(help_text='Дата анализа', verbose_name='Дата')
    value = models.CharField(max_length=10, help_text='Значение', verbose_name='значение')
    norm = models.CharField(max_length=20,
                            blank=True, help_text='Норма', verbose_name='норма')
    patient = models.ForeignKey(auth.get_user_model(),
                                on_delete=models.CASCADE, verbose_name='Пациент')

    def str(self):
        return self.name

    class Meta():
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'
        ordering = ['data', 'name']


class PhotoAnalises(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None,
                              blank=True, null=True, verbose_name='Фото анализа')
    data = models.DateField(help_text='Дата анализа', verbose_name='Дата')
    patient = models.ForeignKey(auth.get_user_model(),
                                on_delete=models.CASCADE, verbose_name='Пациент')
    group = models.ForeignKey('GroupOfAnalysis',
                              on_delete=models.PROTECT,
                              verbose_name='Группа анализов')

    def str(self):
        return f'{self.group} {self.patient}'

    class Meta():
        verbose_name = 'Фото анализа'
        verbose_name_plural = 'Фото анализов'
        ordering = ['patient']


class NameOfAnalysis(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название анализа')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    group = models.ForeignKey('GroupOfAnalysis',
                              on_delete=models.PROTECT,
                              related_name='analysis_name',
                              verbose_name='Группа анализов')

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Название анализа'
        verbose_name_plural = 'Названия анализов'
        ordering = ['name']


class GroupOfAnalysis(models.Model):
    group = models.CharField(max_length=100, db_index=True, verbose_name='Группа анализов')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.group

    class Meta():
        verbose_name = 'Групппа анализов'
        verbose_name_plural = 'Группы анализов'


# class UploadFiles(models.Model):
#     file = models.FileField(upload_to='uploads_model',
#                             blank=True, null=True, default=None, verbose_name='Файл')
#     patient = models.ForeignKey(auth.get_user_model(),
#                                 on_delete=models.CASCADE, verbose_name='Пациент')
