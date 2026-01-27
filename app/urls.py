# techteam2/app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('route/', views.route, name='route'),
]