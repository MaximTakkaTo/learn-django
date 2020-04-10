from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('modules/', include('modules.urls')),
    path('signup/', include('registration.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
