from django.urls import path
from . import views

urlpatterns = [
    path("", views.top, name="top"),
    path("menu/", views.menu, name="menu"),
    path("machines/", views.machine_list, name="machine_list"),
    path("account/", views.account, name="account"),
    path("help/", views.help_view, name="help"),

    path(
        "machines/toggle/<int:machine_id>/",
        views.toggle_machine_status,
        name="toggle_machine_status"
    ),

    path(
        "exercise/add/",
        views.add_exercise_log,
        name="add_exercise_log"
    ),
]