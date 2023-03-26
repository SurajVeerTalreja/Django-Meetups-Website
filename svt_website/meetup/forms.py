from django import forms
# from .models import Participant

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Participant

#         fields = '__all__'

#         labels = {
#             'first_name': 'First Name',
#             'last_name': 'Last Name',
#             'email': 'Your Email',
#         } 

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=70)
    last_name = forms.CharField(max_length=70)
    email = forms.EmailField(label='Your Email:')