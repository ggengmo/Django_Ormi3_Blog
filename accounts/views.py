# accounts > views.py

from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from . models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PasswordForm, ProfileForm

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

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user.profile
    
    # def get_initial(self):
    #     return {'name': '', 'nickname': '', 'email': ''}

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user.email = form.cleaned_data.get('email')
        profile.user.save()
        profile.save()
        return super().form_valid(form)
    
profile_update = ProfileUpdateView.as_view()