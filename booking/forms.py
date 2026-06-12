from django import forms
from .models import SERVICE_CHOICES

class BookingForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=120,
        widget=forms.TextInput(attrs={'placeholder': 'Your full name'}),
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
    )
    phone = forms.CharField(
        label='Phone',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': '07-12-345-678'}),
    )
    service = forms.ChoiceField(
        label='Service',
        choices=SERVICE_CHOICES,
    )
    preferred_datetime = forms.CharField(
        label='Preferred date / time',
        max_length=120,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Friday 3pm'}),
    )
    message = forms.CharField(
        label='Notes',
        required=False,
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Anything else we should know?'}),
    )
