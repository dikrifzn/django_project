from django.contrib import admin
from django.urls import path, include

from . import views
from about import views as aboutViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
]