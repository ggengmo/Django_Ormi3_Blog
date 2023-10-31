# accounts > views.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from . models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PasswordForm

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

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    
    def get_object(self):
        return self.request.user.profile

profile = ProfileView.as_view()

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordForm
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('accounts:profile')

change_password = ChangePasswordView.as_view()
    