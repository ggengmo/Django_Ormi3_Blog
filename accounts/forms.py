# accounts > forms.py

from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile

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
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'name', 'nickname', 'email']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['profile_image'].label = '프로필 사진'
        self.fields['name'].label = '이름'
        self.fields['nickname'].label = '닉네임'
        self.fields['email'].label = '이메일'