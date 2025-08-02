from django.urls import path
from .views.main_view import home, skill, project, contact, about, service, add_project, single_project

urlpatterns = [
    path('', home, name='home'),
    path('skill/',skill, name='skill'),
    path('service/',service, name='service'),
    path('project/', project, name='project'),
    path('contact/',contact, name='contact'),
    path('about/', about, name='about'),
    path('add_project/', add_project, name='add_project'),
    path('single_pgoject/',single_project, name='single_project')
]
