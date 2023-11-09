# accounts > views.py

from typing import Any
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from . models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PasswordForm, ProfileForm, SignUpForm, CustomAuthenticationForm

class SignCreateView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/form.html'

    def get_success_url(self):
        return reverse_lazy('accounts:login')

signup = SignCreateView.as_view()

class LoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'accounts/form2.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        print(next_url)
        if next_url:
            return next_url
        else:
            return reverse_lazy('blog:post_list')

login = LoginView.as_view()

class LogoutView(LogoutView):
    next_page = reverse_lazy('main:index')

    def get_next_page(self):
        next_page = super().get_next_page()
        next_url = self.request.GET.get('next', None)
        if next_url:
            return next_url
        else:
            return next_page

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

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user.email = form.cleaned_data.get('email')
        profile.user.save()
        profile.save()
        return super().form_valid(form)
    
profile_update = ProfileUpdateView.as_view()