from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path(
        "logout/",
        LogoutView.as_view(next_page="/accounts/login/"),
        name="logout"
    ),
]