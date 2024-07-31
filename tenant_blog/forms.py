from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['tenant', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth']
