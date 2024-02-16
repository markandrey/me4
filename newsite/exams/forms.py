from django import forms
from .models import Exam, NameOfExam, PhotoAnalises, GroupOfAnalysis
from django.contrib.auth import get_user_model


class AddExamForm(forms.ModelForm):
    # два поля определяем сами, прописывая ннужные характеристики
    name = forms.ModelChoiceField(queryset=NameOfExam.objects.all(),
                                  empty_label='Выберите исследование', label='Название исследования')
    patient = forms.ModelChoiceField(queryset=get_user_model().objects.all(),
                                     empty_label='Выберите пациента', label='Пациент')

    class Meta:
        model = Exam  # с какой моделью связана форма
        fields = ['name', 'data', 'patient', 'content', 'photo']  # поля, отображаемые в форме


class AddAnalisisForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=GroupOfAnalysis.objects.all(),
                                  empty_label='Выберите вид анализов', label='Анализы')
    patient = forms.ModelChoiceField(queryset=get_user_model().objects.all(),
                                     empty_label='Выберите пациента', label='Пациент')

    class Meta:
        model = PhotoAnalises
        fields = ['group', 'data', 'patient', 'photo']

