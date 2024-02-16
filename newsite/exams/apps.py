from django.apps import AppConfig


class ExamsConfig(AppConfig):
    verbose_name = 'База данных исследований и анализов'  # используется в Админ-панели
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exams'
