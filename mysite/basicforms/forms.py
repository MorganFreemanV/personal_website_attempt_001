from django import forms
from django.core import validators
from django.contrib.auth.models import User

# custom validator
""" def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with z!") """


# first name, last name, email address, password, confirm password

class LoginData(forms.Form):
    first_name = forms.CharField(max_length=264, required=True)
    last_name = forms.CharField(max_length=264, required=True)
    email_add = forms.EmailField(max_length=264, required=True)
    email_add_conf = forms.EmailField(max_length=264, required=True)
    pw1 = forms.CharField(min_length=8, max_length=16, widget=forms.PasswordInput(render_value=True), required=True)
    pw2 = forms.CharField(min_length=8, max_length=16, widget=forms.PasswordInput(render_value=True), required=True)

    def clean(self):
        all_clean_data = super().clean()
        compare_email = (all_clean_data['email_add'] == all_clean_data['email_add_conf'])
        compare_password = (all_clean_data['pw1'] == all_clean_data['pw2'])
        if compare_email == False:
            raise forms.ValidationError('Make sure emails match!')
        if compare_password == False:
            raise forms.ValidationError('Make sure passwords match!')
        if User.objects.filter(email='email_add').exists():
            raise forms.ValidationError('Email exists in system! Please use another email.')


class FormName(forms.Form):
    name = forms.CharField(max_length=256)
    #name = forms.CharField(max_length=256, validators=[check_for_z])
    email = forms.EmailField(max_length=256, widget=forms.EmailInput)
    verify_email = forms.EmailField(label='Enter your email again!')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError('Make sure the emails match!')

    """ 
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('GOTCHA BOT')
        return botcatcher
     """
'''
class LoginForm(forms.Form):
    name = forms.CharField(max_length=256)
    email = forms.EmailField(max_length=256, widget=forms.EmailInput)
    verify_email = forms.EmailField(label='Enter your email again!')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError('Make sure the emails match!')
'''