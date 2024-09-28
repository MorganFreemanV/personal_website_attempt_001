from django import forms
from django.core import validators

# custom validator
""" def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with z!") """

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