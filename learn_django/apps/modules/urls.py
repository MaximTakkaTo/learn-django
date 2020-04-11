from django.urls import path

from . import views

app_name = 'modules'

urlpatterns = [
    path('', views.modules, name = 'modules'),
    path('about/', views.about, name = 'about'),
    path('<str:module_eng_tag>/<str:lesson_eng_tag>/', views.detail, name = 'detail')
]