from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    date_joined = forms.DateTimeField(disabled=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'date_joined']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter User Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        
        # for field_name, field in self.fields.items():
        #     self.fields[field_name].widget.attrs['placeholder'] = field.label

class CreateUserForm(UserCreationForm): 
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'form-control form-control-user', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'form-control form-control-user', 'placeholder': 'Repeat Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-user', "placeholder": "e.g. md_irfan"}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-user', "placeholder": "e.g. Mohd"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-user', "placeholder": "e.g. Irfan"}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-user', "placeholder": "e.g. irfan@gmail.com"}),
        }
