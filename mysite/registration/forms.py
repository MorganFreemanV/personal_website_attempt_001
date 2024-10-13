from django import forms
from registration.models import User
from django.core.exceptions import ValidationError

'''
class UserRegistration(forms.Form):
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
'''
class UserRegistration(forms.ModelForm):
    class Meta():
        model = User
        widgets = {'pw1':forms.PasswordInput(),
                   'pw2':forms.PasswordInput(),
                   }
        fields = '__all__'
    def clean(self):
        all_clean_data = super(UserRegistration, self).clean()
        print(all_clean_data)
        compare_email = (all_clean_data['email_add'] == all_clean_data['email_add_conf'])
        compare_password = (all_clean_data['pw1'] == all_clean_data['pw2'])
        if compare_email == False:
            raise ValidationError('Make sure emails match!')
        if compare_password == False:
            raise ValidationError('Make sure passwords match!')
        if User.objects.filter(email_add='email_add').exists():
            raise ValidationError('Email exists in system! Please use another email.')
        if len(all_clean_data['pw1']) < 8:
            raise ValidationError('Minimum password length is 8!')