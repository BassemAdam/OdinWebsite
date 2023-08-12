from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        #,'Academic qualifications','Experience','Personal Statement','CV','Profile Picture'
        username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Username'}))
        email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Your Username'}))
        password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Your Username'}))
        password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Your Username'}))