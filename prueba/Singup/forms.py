from django import forms

from .models import SingUp

class SingUpForm(forms.ModelForm):
    class Meta:
        model = SingUp
