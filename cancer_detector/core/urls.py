from django.urls import path
from . import views

urlpatterns = [
    path('cancerdetector/', views.home, name='home'),
]

