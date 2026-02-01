from django.urls import path
from . import views

urlpatterns = [
    path("", views.top, name="top"),
    path("menu/", views.menu, name="menu"),
    path("machines/", views.machine_list, name="machine_list"),

    path(
        "machines/toggle/<int:machine_id>/",
        views.toggle_machine_status,
        name="toggle_machine_status"
    ),
    path(
        "exercise/toggle/",
        views.toggle_today_exercise,
        name="toggle_today_exercise"
    ),
]