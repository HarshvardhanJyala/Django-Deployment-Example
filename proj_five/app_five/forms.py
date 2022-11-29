from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from app_five.models import UserProfileInfo


# user is an inbuilt in django which provides itself with username, first name last name email etc.
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
#above one is only for password field, we want it save even admin cannot see it.
    class Meta():
        model = User
        fields = ('username', 'email','password')

#profile info is custom made.. we are adding 2 fields here 1) portfolio_site and 2) pic
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
