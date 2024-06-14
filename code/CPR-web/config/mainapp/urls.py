from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('graph/', views.draw_graph, name='draw_graph'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    path('projects/result/', views.projects_result, name='projects_result'),
    path('contact/', views.contact, name='contact'),
]
