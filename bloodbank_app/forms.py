from django import forms
from django.contrib.auth.forms import UserCreationForm

from bloodbank_app.models import User, Customers, bloodbank, bloodrequest


class DateInput(forms.DateInput):
    input_type = 'Date'
class UserReg(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ('username','password1','password2')

class Customer_reg(forms.ModelForm):
    class Meta:
          model = Customers
          exclude = ('user',)


class Need_blood(forms.ModelForm):
    date_field = forms.DateField(widget=DateInput)
    class Meta:
        model = bloodrequest
        exclude = ('user','Approval_status','Donar_Name','Donar_Age','Donar_BloodType','Donar_Location','Donar_Number')
