from django.urls import path
from resume import views

urlpatterns = [

    path('', views.lunch, name='Lunch'),
    path('home/', views.resu, name='resume'),


]