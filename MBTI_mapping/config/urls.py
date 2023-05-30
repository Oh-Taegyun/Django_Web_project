"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pymap import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('pymap/', include('pymap.urls')),
    path('', views.index),
    path('save_marker_data_E/', views.save_marker_data_E, name='save_marker_data_E'),
    path('get_marker_data_E/', views.get_marker_data_E, name='get_marker_data_E'),
    path('save_marker_data_I/', views.save_marker_data_I, name='save_marker_data_I'),
    path('get_marker_data_I/', views.get_marker_data_I, name='get_marker_data_I'),
    path('form_submit_E/', views.form_submit_E, name='form_submit_E'),
    path('form_submit_I/', views.form_submit_I, name='form_submit_I'),
]
