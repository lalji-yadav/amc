from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(error_messages={'required': 'Enter your username'},
                               widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    email = forms.EmailField(max_length=254, error_messages={'required': 'Enter your email'},
                             widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    password1 = forms.CharField(error_messages={'required': 'Enter your password'},
                                widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    password2 = forms.CharField(error_messages={'required': 'Enter your re-password'},
                                widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class LoginForm(forms.Form):
    username = forms.CharField(error_messages={'required':'Enter your username'},
                               widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    password = forms.CharField(error_messages={'required':'Enter your password'},
                               widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))

