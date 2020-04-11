from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^modules/', include('modules.urls')),
    url(r'^', include('registration.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
