from django import forms

class FormLogin(forms.Form):
    email = forms.EmailField(label="Email", max_length=60)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)