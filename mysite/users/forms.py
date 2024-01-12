from django import forms

class loginform(forms.Form):
    username = forms.CharField(min_length=8, max_length=25, strip=True)
    password = forms.CharField(min_length=8, max_length=18, widget=forms.PasswordInput)
    