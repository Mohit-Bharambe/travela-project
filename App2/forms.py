from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking, Contact


class BookingForm(forms.ModelForm):
    '''Form for tour bookings'''
    
    class Meta:
        model = Booking
        fields = ['name', 'email', 'datetime', 'destination', 'persons', 'category', 'special_request']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control bg-white border-0',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-white border-0',
                'placeholder': 'Your Email'
            }),
            'datetime': forms.DateTimeInput(attrs={
                'class': 'form-control bg-white border-0',
                'placeholder': 'Date & Time',
                'type': 'datetime-local'
            }),
            'destination': forms.TextInput(attrs={
                'class': 'form-control bg-white border-0',
                'placeholder': 'Destination'
            }),
            'persons': forms.NumberInput(attrs={
                'class': 'form-control bg-white border-0',
                'placeholder': 'Number of Persons',
                'min': '1'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select bg-white border-0'
            }),
            'special_request': forms.Textarea(attrs={
                'class': 'form-control bg-white border-0',
                'placeholder': 'Special Request',
                'rows': 4
            }),
        }


class ContactForm(forms.ModelForm):
    '''Form for contact submissions'''
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control border-0',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-0',
                'placeholder': 'Your Email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control border-0',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control border-0',
                'placeholder': 'Leave a message here',
                'rows': 6
            }),
        }


class UserRegistrationForm(UserCreationForm):
    '''Extended user registration form'''
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
