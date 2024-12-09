from django import forms  # Importa o módulo forms do Django para criar formulários.
from django.core.exceptions import ValidationError  # Importa a exceção ValidationError para validação personalizada de campos.

# Formulário para login de usuários
class FormLogin(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Informe seu nome de usuário'}), max_length=60)  # Campo de texto para o nome de usuário, com placeholder.
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Informe sua senha', 'id': 'id_passwordLogin'}), min_length=8)  # Campo de senha com mínimo de 8 caracteres.

# Formulário para criar uma nova turma
class FormNovaTurma(forms.Form):
    nome_da_turma = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nome da Turma'}), max_length=60)  # Campo de texto para nome da turma.
    arquivo = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'custom-file-label', 'id': 'file-upload'})  # Campo de upload de arquivo.
    )

    # Validação personalizada para garantir que o arquivo seja do tipo .xlsx
    def clean_arquivo(self):
        arquivo = self.cleaned_data.get('arquivo')
        if arquivo:
            if not arquivo.name.endswith('.xlsx'):
                raise ValidationError("Apenas arquivos .xlsx são permitidos.")
        return arquivo

# Formulário para cadastro de usuários
class FormCadastro(forms.Form):
    email = forms.CharField(label="E-mail", widget=forms.EmailInput(attrs={'placeholder':'Email', 'class': 'form-control'}), max_length=60)  # Campo para email.
    user = forms.CharField(label="Nome de Usuário", max_length=50, widget=forms.TextInput(attrs={'placeholder':'User', 'class': 'form-control'}))  # Campo para nome de usuário.
    first_name = forms.CharField(label="Nome", max_length=80, widget=forms.TextInput(attrs={'placeholder':'Nome', 'class': 'form-control'}))  # Campo para nome completo.
    password = forms.CharField(required=True,label="Senha Geenfy", widget=forms.PasswordInput(attrs={'placeholder':'Senha', 'id': 'id_passwordCadastro', 'class': 'form-control'}), min_length=8)  # Campo para senha.
    new_password = forms.CharField(label="Nova Senha Geenfy", widget=forms.PasswordInput, required=False)  # Campo opcional para nova senha.

    # Personalização do formulário: torna o campo de senha opcional no modo de edição
    def __init__(self, *args, is_editing=False, **kwargs):
        super(FormCadastro, self).__init__(*args, **kwargs)
        if is_editing:
            self.fields['password'].required = False  # Senha não é obrigatória em modo de edição.

# Formulário para informações adicionais de cadastro
class FormCadastro_Info(forms.Form):
    LoginCAF = forms.CharField(label="Login CAF", max_length=100, widget=forms.TextInput(attrs = {'class': 'form-control'}))  # Campo para login CAF.
    SenhaCAF = forms.CharField(required=True, label="Senha CAF", widget=forms.PasswordInput(attrs = {'class': 'form-control'}))  # Campo para senha CAF.
    LoginIHX = forms.CharField(label="Login IHX", max_length=100, widget=forms.TextInput(attrs = {'class': 'form-control'}))  # Campo para login IHX.
    SenhaIHX = forms.CharField(required=True, label="Senha IHX", widget=forms.PasswordInput(attrs = {'class': 'form-control'}))  # Campo para senha IHX.

    # Personalização do formulário: torna os campos de senha opcionais no modo de edição
    def __init__(self, *args, is_editing=False, **kwargs):
        super(FormCadastro_Info, self).__init__(*args, **kwargs)
        if is_editing:
            self.fields['SenhaIHX'].required = False  # Senha IHX não obrigatória em modo de edição.
            self.fields['SenhaCAF'].required = False  # Senha CAF não obrigatória em modo de edição.
