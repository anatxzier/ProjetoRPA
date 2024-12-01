from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import authenticate, login
from geenfy.models import Cadastro, Usuario  # Certifique-se de que o modelo Cadastro está na aplicação correta
from geenfy.forms import FormCadastro  # Certifique-se de que o formulário está na aplicação correta

class ViewTest(TestCase):

    def setUp(self):
        # Criar grupos e usuários conforme necessário
        self.group_coordenador = Group.objects.create(name='Coordenador')
        self.group_funcionario = Group.objects.create(name='funcionario')

        self.coordenador = User.objects.create_user(username='coordenador_teste', password='coordenador123')
        self.coordenador.groups.add(self.group_coordenador)

        self.usuario_comum = User.objects.create_user(username='usuario_comum', password='comum123')
        self.usuario_comum.groups.add(self.group_funcionario)

        # Criar funcionários para testes de exclusão
        self.funcionario = User.objects.create_user(username='funcionario_teste', password='funcionario123')
        self.funcionario.groups.add(self.group_funcionario)

        # Criar um usuário no modelo Usuario
        self.usuario = User.objects.create_user(username='usuario_teste', password='usuario123')
        self.usuario.groups.add(self.group_funcionario)

        self.usuario_info, created = Usuario.objects.get_or_create(user=self.usuario)

        # Se o usuário foi criado e os campos de login e senha estão vazios, preenchê-los
        if created or not self.usuario_info.login_CAF or not self.usuario_info.senha_CAF or not self.usuario_info.login_IHX or not self.usuario_info.senha_IHX:
            self.usuario_info.login_CAF = 'usuario_caf'
            self.usuario_info.senha_CAF = '12345_caf'
            self.usuario_info.login_IHX = 'usuario_ihx'
            self.usuario_info.senha_IHX = '12345_ihx'
            self.usuario_info.save()

        # URLs
        self.url_login = reverse('login')
        self.url_novaturma = reverse('novaturma')
        self.url_cadastro = reverse('cadastro')
        self.url_cadinfo = reverse('cadinfo')  
        self.url_excluir = reverse('excluir_funcionario')


   #Login/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def test_login_view_redirecionamento_completo(self):
        """Testa se o usuário é redirecionado corretamente após login com informações completas"""
        response = self.client.post(self.url_login, {'user': 'usuario_teste', 'password': 'usuario123'})
       
        self.assertEqual(response.status_code, 302)  # Redirecionamento após login
        # Como o usuário tem login_CAF e login_IHX, ele deve ser redirecionado para 'novaturma'
        self.assertRedirects(response, self.url_novaturma)


    def test_login_view_redirecionamento_incompleto(self):
        """Testa se o usuário é redirecionado para 'cadinfo' quando falta informações"""
        # Modificando o usuário para que falte algum dado de login
        usuario = Usuario.objects.get(user=self.usuario)  # Acessando o modelo Usuario, não o User diretamente
        usuario.login_CAF = ""
        usuario.save()

        response = self.client.post(self.url_login, {'user': 'usuario_teste', 'password': 'usuario123'})
        self.assertEqual(response.status_code, 302)  # Redirecionamento após login

        # Como o usuário não tem login_CAF, ele deve ser redirecionado para 'cadinfo'
        self.assertRedirects(response, self.url_cadinfo)

    def test_login_view_com_usuario_invalido(self):
        """Testa o login com um usuário inválido"""
        response = self.client.post(self.url_login, {'user': 'usuario_invalido', 'password': 'senha_errada'})
        self.assertEqual(response.status_code, 200)  # Não deve redirecionar
        self.assertContains(response, 'Usuário ou senha incorretos')  # Verifica mensagem de erro

    #Exclusão//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def test_exclusao_funcionario(self):
        """Testa a exclusão de um funcionário"""
        # Realizar login como coordenador
        self.client.login(username='coordenador_teste', password='coordenador123')
        # Verificar se o funcionário existe antes da exclusão
        self.assertEqual(User.objects.filter(username='funcionario_teste').count(), 1)
        # Testar exclusão do funcionário
        response = self.client.post(self.url_excluir, {'funcionario_id': self.funcionario.id})
        # Verifica se o redirecionamento ocorreu corretamente
        self.assertRedirects(response, reverse('funcionarios'))
        # Verificar se o funcionário foi excluído
        self.assertEqual(User.objects.filter(username='funcionario_teste').count(), 0)


    def test_exclusao_funcionario_sem_permissao(self):
        """Testa se um usuário comum não pode excluir um funcionário"""
        # Realizar login como usuário comum
        self.client.login(username='usuario_comum', password='comum123')

        # Tentar excluir o funcionário
        response = self.client.post(self.url_excluir, {'funcionario_id': self.funcionario.id})
        self.assertEqual(User.objects.filter(username='funcionario_teste').count(), 1)  # Verifica se o funcionário não foi excluído
        self.assertRedirects(response, reverse('home'))  # Redireciona para outra página

   
    #Cadastro/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def test_cadastro_view_permissao_coordenador(self):
        """Testa se apenas o coordenador pode acessar a página de cadastro"""
        # Realizar login como coordenador
        self.client.login(username='coordenador_teste', password='coordenador123')

        response = self.client.get(self.url_cadastro)
        self.assertEqual(response.status_code, 200)  # Página carregada com sucesso
        self.assertTemplateUsed(response, 'cadastro.html')

    def test_cadastro_view_sem_permissao(self):
        """Testa se um usuário comum não pode acessar a página de cadastro"""
        # Realizar login como usuário comum
        self.client.login(username='usuario_comum', password='comum123')

        response = self.client.get(self.url_cadastro)
        self.assertRedirects(response, reverse('home'))  # Verifica se redirecionou para a URL 'home'

    def test_cadastro_usuario_sucesso(self):
        """Testa se o cadastro de um novo usuário é feito com sucesso"""
        # Realizar login como coordenador
        self.client.login(username='coordenador_teste', password='coordenador123')

        response = self.client.post(self.url_cadastro, {
            'first_name': 'Novo',
            'user': 'novo_usuario',
            'email': 'novo@teste.com',
            'password': 'nova_senha'
        })

        # Verificar se o usuário foi criado e redirecionado para a página de cadastro
        self.assertEqual(User.objects.count(), 5)  # Verifica se o novo usuário foi criado
        self.assertRedirects(response, reverse('cadastro'))
    
    def test_cadastro_usuario_existente(self):
        """Testa se exibe mensagem de erro quando o nome de usuário já existe"""
        # Realizar login como coordenador
        self.client.login(username='coordenador_teste', password='coordenador123')

        # Criar um usuário para testar a duplicidade
        User.objects.create_user(username='usuario_existente', password='senha123')

        response = self.client.post(self.url_cadastro, {
            'first_name': 'Test',
            'user': 'usuario_existente',
            'email': 'email@test.com',
            'password': 'senha123'
        })
        self.assertContains(response, 'Nome de usuário já existe, por favor tente novamente')
