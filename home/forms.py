from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter username',
        'class': 'form-control bg-transparent text-light',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Email',
        'class': 'form-control bg-transparent text-light',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control bg-transparent text-light',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password',
        'class': 'form-control bg-transparent text-light',
    }))


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter username',
        'class': 'form-control bg-transparent text-light',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control bg-transparent text-light',
    }))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'role', 'comment', 'image',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control bg-transparent text-light',
                'aria-label': 'form-control',
                'id': 'name',
                'placeholder': 'Your Name',
            }),

            'role': forms.TextInput(attrs={
                'class': 'form-control bg-transparent text-light',
                'aria-label': 'form-control',
                'id': 'role',
                'placeholder': 'Your Title',
            }),

            'comment': forms.Textarea(attrs={
                'class': 'form-control bg-transparent text-light',
                'aria-label': 'With textarea',
                'id': 'comment',
                'placeholder': 'Say Something Nice 😊',
            }),

            'image': forms.FileInput(attrs={
                'class': 'form-control bg-transparent text-light',
                'id': 'customFile',
                'label': 'Select an Image (optional)',
                'placeholder': 'Upload an image (Optional)',
            }),
            
        }


class MessagesForm(forms.ModelForm):
    # Adding custom attributes to the username field
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'placeholder': 'Your Name'

    }))

    # Adding email field with 'required' attribute
    email = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'placeholder': 'Your Email.'

    }))

    # Adding Phone number field with 'required' attribute
    phone = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'num',
        'placeholder': 'Your Phone Number.',
        
    }))

    # Adding first_name field with 'required' attribute and max length
    subject = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'subject',
        'placeholder': 'Subject.'

    }))

    # Adding last_name field with 'required' attribute and max length
    message = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'message',
        'placeholder': 'Your message here...'
    }))

    class Meta:
        model = Messages  # Assuming User is your custom User model
        fields = ('name', 'email', 'phone', 'subject', 'message')
