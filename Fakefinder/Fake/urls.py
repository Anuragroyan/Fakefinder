from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Homepage'),
    path('index/', views.index, name='Main-fakefinder'),
    path('index/predict', views.predict, name='Predictpage'),
]