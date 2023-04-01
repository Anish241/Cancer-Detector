from django.urls import path
from . import views

urlpatterns = [

    path('cancerdetector/', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('menu/brain/', views.brain, name='brain'),

]

