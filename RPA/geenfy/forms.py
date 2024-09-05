from django import forms
from django.core.exceptions import ValidationError

class FormLogin(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Informe seu email'}), max_length=60)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Informe sua senha'}), min_length=8)

class FormNovaTurma(forms.Form):
    LoginCAF = forms.CharField(label="Login CAF", max_length=100)
    SenhaCAF = forms.CharField(label="Senha CAF", widget=forms.PasswordInput)
    LoginIHX = forms.CharField(label="Login IHX", max_length=100)
    SenhaIHX = forms.CharField(label="Senha IHX", widget=forms.PasswordInput)
    arquivo = forms.FileField(label="Arquivo")

    def clean_arquivo(self):
        arquivo = self.cleaned_data.get('arquivo')

        if arquivo:
            if not arquivo.name.endswith('.xlsx'):
                raise ValidationError("Apenas arquivos .xlsx são permitidos.")
                
        return arquivo

class FormCadastro(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email'}), max_length=60)
    user = forms.CharField( max_length=50, widget=forms.TextInput(attrs={'placeholder':'User'}))
    first_name = forms.CharField ( max_length=80, widget=forms.TextInput(attrs={'placeholder':'Nome'}))
    password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Senha'}), min_length=8)    