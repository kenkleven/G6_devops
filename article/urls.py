from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='accueil'),
    path('details/<str:pk>/', views.details, name='details'),
]
