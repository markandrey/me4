from django.contrib import auth
# from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, TemplateView, ListView
#
# from .forms import AddExamForm, UploadFileForm
# from .models import Exam, UploadFiles, Analysis
from .utils import menu, DataMixin


class First(DataMixin, TemplateView):
    template_name = 'exams/index.html'
    title_page = 'Главная страница'
    message = f"Добро пожаловать на сайт! Уже зарегистрировано {auth.get_user_model().objects.count()} участников!"


def show_all(request):
    # all_exams = Exam.objects.filter(patient=request.user.pk)
    all_exams = []
    # all_ans = Analysis.objects.filter(patient=request.user.pk)
    all_ans = []

    data = {
        'title': 'Вся медицинская информация.',
        'menu': menu,
        "all_exams": all_exams,
        "all_ans": all_ans,
    }
    return render(request,"exams/show_all.html", context=data)


def info(request):
    # if request.method == 'POST':
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         fp = UploadFiles(file=form.cleaned_data['file'], patient=request.user)
    #         fp.save()
    # else:
    #     form = UploadFileForm()
    form = ''

    data = {
        'title': 'Добавление результата',
        'menu': menu,
        'form': form,
    }
    return render(request, 'exams/file_upload.html', context=data)
