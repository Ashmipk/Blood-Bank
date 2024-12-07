from django import forms
from django.contrib.auth.forms import UserCreationForm

from bloodbank_app.models import User, bloodbank


class UserReg(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ('username','password1','password2')

class bloodbank_reg(forms.ModelForm):
    class Meta:
          model = bloodbank
          exclude = ('user',)
