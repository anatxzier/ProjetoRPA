from django import forms

class FormLogin(forms.Form):
    email = forms.EmailField(label="Email", max_length=60)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class FormNovaTurma(forms.Form):
    LoginCAF = forms.CharField(label="Login CAF", max_length=100)
    SenhaCAF = forms.CharField(label="Senha CAF", widget=forms.PasswordInput)
    LoginIHX = forms.CharField(label="Login IHX", max_length=100)
    SenhaIHX = forms.CharField(label="Senha IHX", widget=forms.PasswordInput)
    arquivo = forms.FileField(label="Arquivo")