from django.urls import path
from pro import views



urlpatterns = [
    path('projects/', views.projects, name='projects'),


]
