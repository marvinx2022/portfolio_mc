from django.contrib import admin
from django.urls import path
from portfolio.views import index, education, footer, header, projects, services, stack, about, management

urlpatterns = [
    
    path('', index, name='Index'),
    path('about', about, name='About'),
    path('education', education, name='Education'),
    path('footer', footer, name='Footer'),
    path('header', header, name='Header'),
    path('projects', projects, name='Projects'),
    path('services', services, name='Services'),
    path('stack', stack, name='Stack'),
    path('management', management, name='Management')

]