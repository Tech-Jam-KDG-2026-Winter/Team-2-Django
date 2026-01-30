from django.urls import path
from . import views

urlpatterns = [
    path("", views.top, name="top"),
    path("menu/", views.menu, name="menu"),
    path("machines/", views.machine_list, name="machine_list"),
]