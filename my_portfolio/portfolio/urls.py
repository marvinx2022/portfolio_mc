from django.contrib import admin
from django.urls import path
from portfolio.views import index

urlpatterns = [
    path('', index, name='Index'),
]