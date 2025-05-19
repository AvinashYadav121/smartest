
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
    
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

class HousePredictionForm(forms.Form):
    total_sqft = forms.FloatField(label='Total Square Feet')
    bath = forms.IntegerField(label='Number of Bathrooms')
    bhk = forms.IntegerField(label='Number of Bedrooms (BHK)')
    location = forms.ChoiceField(label='Location')

    def __init__(self, *args, **kwargs):
        locations = kwargs.pop('locations', [])
        super().__init__(*args, **kwargs)
        self.fields['location'].choices = [(loc, loc.title()) for loc in locations]



#registering the custom user model

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_image', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

