
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect

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




class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email

    

# def logout_view(request):
#     logout(request)
#     return redirect('home')


