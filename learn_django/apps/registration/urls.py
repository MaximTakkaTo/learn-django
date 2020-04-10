from django.urls import path, include
from . import views

app_name = 'registration'

urlpatterns = [
    path('', views.signup, name = 'signup')
]