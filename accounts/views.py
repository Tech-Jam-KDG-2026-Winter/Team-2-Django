from django.contrib.auth.views import LoginView
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'