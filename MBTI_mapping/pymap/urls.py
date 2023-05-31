from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('form_submit_E/', views.form_submit_E, name='form_submit_E'),
    path('form_submit_I/', views.form_submit_I, name='form_submit_I'),
]
