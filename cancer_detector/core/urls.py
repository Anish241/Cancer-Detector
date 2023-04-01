from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('cancerdetector/', views.home, name='home'),
=======
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('menu/brain/', views.brain, name='brain'),
>>>>>>> db5877f (brain model created)
]

