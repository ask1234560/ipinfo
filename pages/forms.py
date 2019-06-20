from django import forms

class Form(forms.Form):
    ip=forms.CharField(max_length=20)

