# Generated by Django 5.0.2 on 2024-02-11 15:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupOfAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(db_index=True, max_length=100, verbose_name='Группа анализов')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Групппа анализов',
                'verbose_name_plural': 'Группы анализов',
            },
        ),
        migrations.CreateModel(
            name='NameOfExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название исследования')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Название исследования',
                'verbose_name_plural': 'Названия исследований',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='NameOfAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название анализа')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='analysis_name', to='exams.groupofanalysis', verbose_name='Группа анализов')),
            ],
            options={
                'verbose_name': 'Название анализа',
                'verbose_name_plural': 'Названия анализов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(help_text='Дата анализа', verbose_name='Дата')),
                ('value', models.CharField(help_text='Значение', max_length=10, verbose_name='значение')),
                ('norm', models.CharField(help_text='Норма', max_length=20, verbose_name='норма')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пациент')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='analysis_name', to='exams.nameofanalysis', verbose_name='Название анализа')),
            ],
            options={
                'verbose_name': 'Анализ',
                'verbose_name_plural': 'Анализы',
                'ordering': ['data', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Дата исследования')),
                ('content', models.TextField(verbose_name='Заключение')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото исследования')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пациент')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='exam_name', to='exams.nameofexam', verbose_name='Название исследования')),
            ],
            options={
                'verbose_name': 'Обследование',
                'verbose_name_plural': 'Обследования',
                'ordering': ['data'],
            },
        ),
        migrations.CreateModel(
            name='PhotoAnalises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото анализа')),
                ('data', models.DateField(help_text='Дата анализа', verbose_name='Дата')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exams.groupofanalysis', verbose_name='Группа анализов')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Фото анализа',
                'verbose_name_plural': 'Фото анализов',
                'ordering': ['patient'],
            },
        ),
    ]
