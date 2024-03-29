from django.urls import path
from . import views


urlpatterns = [
    path('', views.First.as_view(), name='home'),
    path('nutrition/', views.ShowNutrition.as_view(), name='nutrition'),
    path('activity/', views.ShowActivity.as_view(), name='activity'),
    path('bmi/', views.BMI.as_view(), name='bmi'),
    path('medicines/', views.AboutMedicines.as_view(), name='about_medicines'),
    path('doc/', views.AboutDoc.as_view(), name='about_doc'),
    path('showall/', views.ShowCaseHistory.as_view(), name='all'),  # показать историю болезни авторизированнного пользователя
    path('addexam/', views.AddExam.as_view(), name='add_exam')
]
