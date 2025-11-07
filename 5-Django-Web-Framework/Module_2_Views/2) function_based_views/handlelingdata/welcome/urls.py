from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('hello_anas/', views.hello_anas, name='hello_anas'),
    path('current_time/', views.current_time, name='current_time'),
    path('message/', views.message, name='message'),
]