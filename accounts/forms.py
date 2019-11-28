from django import forms


class UserLoginForm(forms.form):
    """Form to be used to log users in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
