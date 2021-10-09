from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import  Resume

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, 
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"),
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'current-password','autofocus':True,'class':'form-control'}))

    new_password1 = forms.CharField(label=_("New Password"),
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password','autofocus':True,'class':'form-control'}),

    help_text=password_validation.password_validators_help_text_html())
    
    new_password2 = forms.CharField(label=_("Confirm New Password"),
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password','autofocus':True,'class':'form-control'}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label= _("Email"), max_length=254,
    widget=forms.EmailInput(attrs={'autocomplete':'email',
    'class':'form-control'})),

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"),
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password','autofocus':True,'class':'form-control'}),

    help_text=password_validation.password_validators_help_text_html())
    
    new_password2 = forms.CharField(label=_("Confirm New Password"),
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password','autofocus':True,'class':'form-control'}))



class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields =['id','name','role','location','experience','skills','organization',
                'salary','startdate','position','gap','age','qualification','my_file']
        labels = {'name':'Full Name', 'role': 'Role', 'location':'Location', 'experience':'Experience ', 'skills':'Skills', 'organization':'Organization','salary':'Salary','startdate':'Start Date','position':'Position','gap':'Gap','age':'Age', 'qualification':'Qualification','my_file':'Document'}
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'role':forms.TextInput(attrs={'class':'form-control'}),
        'location':forms.TextInput(attrs={'class':'form-control'}),
        'experience':forms.NumberInput(attrs={'class':'form-control'}),
        'skills':forms.TextInput(attrs={'class':'form-control'}),
        'organization':forms.TextInput(attrs={'class':'form-control'}),
        'salary':forms.NumberInput(attrs={'class':'form-control'}),
        'startdate':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
        'position':forms.TextInput(attrs={'class':'form-control'}),
        'gap':forms.NumberInput(attrs={'class':'form-control'}),
        'age':forms.TextInput(attrs={'class':'form-control'}),
        'qualification':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        }