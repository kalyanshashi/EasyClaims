from django import forms
from .models import List


class ListForm(forms.ModelForm):
    class Meta:
        model=List
        fields=["name","dob","address","policyNo","typeOfClaim","details","docs"]
