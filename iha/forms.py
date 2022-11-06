#input alanı oluşturma
from django import forms
from .models import Iha
class IhaForm(forms.ModelForm):
    class Meta :
        model = Iha
        fields=["marka","model","category","weight","image"]