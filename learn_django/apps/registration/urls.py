from django.urls import path, include
from . import views

app_name = 'registration'

urlpatterns = [
    path('', views.signin, name = 'signin'),
    path('signup/', views.signup, name = 'signup'),
    path('verify/<str:uuid>/', views.verify, name = 'verify'),
    path('logout', views.log_out, name = 'logout')
]