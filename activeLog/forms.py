from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import pytz
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))    

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    timezone = forms.ChoiceField(choices=TIMEZONES)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','timezone', 'password1', 'password2', )