from django.contrib import admin
from .models import Exam, NameOfExam, NameOfAnalysis, GroupOfAnalysis, Analysis


# прописываем класс для настройки вывода модели в Админ-панели
# декоратор - регистрирует модель
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['patient', 'name', 'data', 'content', 'confirmed']
    list_display_links = ['patient', 'name']  # кликабельные поля
    ordering = ['patient', 'data']  # сортировка (только для Админн-панели)
    list_editable = ['confirmed']


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ['patient', 'name', 'data', 'value', 'norm']
    list_display_links = ['patient', 'name']
    ordering = ['patient', 'data']
    list_editable = ['norm']  # редактируемое из АП поле, не может быть кликабельным


@admin.register(NameOfExam)
class NameExamAdmin(admin.ModelAdmin):
    ordering = ['name']
    prepopulated_fields = {'slug': ['name']}  # автоматически заполняет поле slug


@admin.register(NameOfAnalysis)
class NameAnalysisAdmin(admin.ModelAdmin):
    ordering = ['name']
    prepopulated_fields = {'slug': ['name']}  # автоматически заполняет поле slug


@admin.register(GroupOfAnalysis)
class GroupAnalysisAdmin(admin.ModelAdmin):
    ordering = ['group']
    prepopulated_fields = {'slug': ['group']}  # автоматически заполняет поле slug

