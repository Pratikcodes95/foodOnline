from .models import User
from django import forms

class Userforms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class meta:
        model = User
        fields = ['first_name','last_name','username','email',
                  'phone_number','password','confirm_password']
