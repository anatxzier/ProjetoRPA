from django import forms
from django.core.exceptions import ValidationError

class FormLogin(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Informe seu nome de usuário'}), max_length=60)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Informe sua senha', 'id': 'id_passwordLogin'}), min_length=8)

class FormNovaTurma(forms.Form):
    nome_da_turma = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nome da Turma'}), max_length=60)
    arquivo = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'custom-file-label', 'id': 'file-upload'})
    )

    def clean_arquivo(self):
        arquivo = self.cleaned_data.get('arquivo')

        if arquivo:
            if not arquivo.name.endswith('.xlsx'):
                raise ValidationError("Apenas arquivos .xlsx são permitidos.")
                
        return arquivo

class FormCadastro(forms.Form):
    email = forms.CharField(label="E-mail", widget=forms.EmailInput(attrs={'placeholder':'Email', 'class': 'form-control'}), max_length=60)
    user = forms.CharField(label="Nome de Usuário", max_length=50, widget=forms.TextInput(attrs={'placeholder':'User', 'class': 'form-control'}))
    first_name = forms.CharField(label="Nome", max_length=80, widget=forms.TextInput(attrs={'placeholder':'Nome', 'class': 'form-control'}))
    password = forms.CharField( required=True,label="Senha Geenfy", widget=forms.PasswordInput(attrs={'placeholder':'Senha', 'id': 'id_passwordCadastro', 'class': 'form-control'}), min_length=8)
    new_password = forms.CharField(label="Nova Senha Geenfy", widget=forms.PasswordInput, required=False)

    def __init__(self, *args, is_editing=False, **kwargs):
        super(FormCadastro, self).__init__(*args, **kwargs)
        if is_editing:
            # Torna o campo de senha opcional no modo de edição
            self.fields['password'].required = False

class FormCadastro_Info(forms.Form):
    LoginCAF = forms.CharField(label="Login CAF", max_length=100, widget=forms.TextInput(attrs = {'class': 'form-control'}))
    SenhaCAF = forms.CharField(required=True, label="Senha CAF", widget=forms.PasswordInput(attrs = {'class': 'form-control'}))
    LoginIHX = forms.CharField(label="Login IHX", max_length=100, widget=forms.TextInput(attrs = {'class': 'form-control'}))
    SenhaIHX = forms.CharField(required=True, label="Senha IHX", widget=forms.PasswordInput(attrs = {'class': 'form-control'}))

    def __init__(self, *args, is_editing=False, **kwargs):
        super(FormCadastro_Info, self).__init__(*args, **kwargs)
        if is_editing:
            # Torna os campos de senha opcionais no modo de edição
            self.fields['SenhaIHX'].required = False
            self.fields['SenhaCAF'].required = False