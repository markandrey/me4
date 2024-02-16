from django.contrib import auth
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, TemplateView, ListView

from .forms import AddExamForm
from .models import Exam, Analysis
from .utils import menu, DataMixin


class First(DataMixin, TemplateView):
    template_name = 'exams/index.html'
    title_page = 'Главная страница'
    message = f"Добро пожаловать на сайт! Уже зарегистрировано {auth.get_user_model().objects.count()} участников!"


class ShowCaseHistory(DataMixin, TemplateView):
    template_name = "exams/show_all.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Данные медицинских исследований и анализов"
        context['exams_lst'] = Exam.objects.filter(patient=self.request.user.pk)
        context['analyses_lst'] = Analysis.objects.filter(patient=self.request.user.pk)
        return context


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


class AddExam(DataMixin, FormView):
    form_class = AddExamForm
    template_name = 'exams/addexam.html'
    success_url = reverse_lazy('home')
    title_page = 'Добавление результата исследования'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# далее - представления из левого бокового меню

class ShowNutrition(DataMixin, TemplateView):
    template_name = 'exams/show_nutrition.html'


class ShowActivity(DataMixin, TemplateView):
    template_name = 'exams/show_activity.html'


class BMI(DataMixin, TemplateView):
    template_name = 'exams/show_bmi.html'


class AboutMedicines(DataMixin, TemplateView):
    template_name = 'exams/about_medicines.html'


class AboutDoc(DataMixin, TemplateView):
    template_name = 'exams/about_doc.html'
