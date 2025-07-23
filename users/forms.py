from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    password_confirm = forms.CharField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if (password and password_confirm) and (password != password_confirm):
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)