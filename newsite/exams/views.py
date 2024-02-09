from django.contrib import auth
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, TemplateView, ListView
#
# from .forms import AddExamForm, UploadFileForm
# from .models import Exam, UploadFiles, Analysis
from .utils import menu, DataMixin


class First(DataMixin, TemplateView):
    template_name = 'exams/index.html'
    title_page = 'Главная страница'
    message = f"Добро пожаловать на сайт! Уже зарегистрировано участников!"
    # message = f"Добро пожаловать на сайт! Уже зарегистрировано {auth.get_user_model().objects.count()} участников!"
