from django.db import models
#from django.core.exceptions import ValidationError

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email_add = models.EmailField(max_length=264, unique=True)
    email_add_conf = models.EmailField(max_length=264, unique=True)
    pw1 = models.CharField(max_length=16)
    pw2 = models.CharField(max_length=16)
    '''
    def clean(self):
        all_clean_data = super().clean()
        compare_email = (all_clean_data['email_add'] == all_clean_data['email_add_conf'])
        compare_password = (all_clean_data['pw1'] == all_clean_data['pw2'])
        if compare_email == False:
            raise ValidationError('Make sure emails match!')
        if compare_password == False:
            raise ValidationError('Make sure passwords match!')
        if User.objects.filter(email='email_add').exists():
            raise ValidationError('Email exists in system! Please use another email.')
        if len(self.pw1) < 8:
            raise ValidationError('Minimum password length is 8!')
    '''