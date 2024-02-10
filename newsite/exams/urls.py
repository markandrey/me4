from django.urls import path
from . import views


urlpatterns = [
    path('', views.First.as_view(), name='home'),
    path('show_all/', views.show_all, name='all'),  # показать историю болезни авторизированнного пользователя
    # path('addanalysis/', views.AddAnalysis.as_view(), name='add_analysis'),
    # path('addexam/', views.AddExam.as_view(), name='add_exam'),
    # path('exam/<int:exam_id>/', views.show_exam, name='exam'),
    path('info/', views.info, name='send_info'),  # загрузка файлов от пациентов
    # path('category/<int:cat_id>/', views.show_category, name='category'),
]
