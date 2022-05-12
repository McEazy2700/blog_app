from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class SignInView(LoginView):
    template_name = 'accounts/signin.html'
    success_url = reverse_lazy('homepage')
