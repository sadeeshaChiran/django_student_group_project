from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreateForm

from django.contrib.auth.views import LoginView

# Create your views here.

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "students/signup.html"


class Login(LoginView):
    template_name = 'students/login.html'

    def get_success_url(self):
        return reverse_lazy('home') 
