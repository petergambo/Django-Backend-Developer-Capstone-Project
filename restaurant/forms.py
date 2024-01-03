from django import forms
from .models import Booking
from django.contrib.auth.models import User

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking  # Use 'model' instead of 'Model'
        fields = "__all__"  # Use 'fields' instead of 'Field'
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = User  # Use 'model' instead of 'Model'
        fields = "__all__"  # Use 'fields' instead of 'Field'
