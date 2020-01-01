from django import forms
from django.contrib.auth.models import User
from app_1.models import ProfileUserInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['username','email','password']

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = ProfileUserInfo
        fields = ['user','portfolio_site','profile_pic']
