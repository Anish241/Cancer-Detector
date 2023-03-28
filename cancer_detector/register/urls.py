from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('approve/', views.approve, name='approve'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
]