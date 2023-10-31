# accounts > forms.py

from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "기존 비밀번호"},
        )
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "변경할 비밀번호"})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "변경할 비밀번호 확인"})
    )

    def clean(self):
        old_password = self.cleaned_data.get("old_password")
        new_password1 = self.cleaned_data.get("new_password1")

        if old_password == new_password1:
            self.add_error(
                "old_password",
                forms.ValidationError("기존 비밀번호와 변경할 비밀번호가 같습니다."),
            )
        else:
            return self.cleaned_data