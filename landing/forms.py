from django import forms
from . models import *

class CallForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = [""]

        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Введите Ваше ФИО ...'}),
            'Email': forms.TextInput(attrs={'placeholder': 'Ваш e-mail ...'}),
            'Phone': forms.TextInput(attrs={'placeholder': '+7 (XXX) XXX-XX-XX'}),
        }
