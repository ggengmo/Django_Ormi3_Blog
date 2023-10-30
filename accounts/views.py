# accounts > views.py

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class SignCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/form.html'
    success_url = reverse_lazy('accounts:login')

signup = SignCreateView.as_view()

class LoginView(LoginView):
    template_name = 'accounts/form.html'

    def get_success_url(self):
        return reverse_lazy('main:index')

login = LoginView.as_view()

class LogoutView(LogoutView):
    next_page = reverse_lazy('main:index')

logout = LogoutView.as_view()