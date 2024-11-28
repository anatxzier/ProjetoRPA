from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import authenticate, login
from geenfy.models import Cadastro  # Certifique-se de que o modelo Cadastro está na aplicação correta
from geenfy.forms import FormCadastro  # Certifique-se de que o formulário está na aplicação correta

class CadastroViewTest(TestCase):

    def setUp(self):
        # Criar grupos
        self.group_coordenador = Group.objects.create(name='Coordenador')
        self.group_funcionario = Group.objects.create(name='funcionario')

        # Criar usuários
        self.coordenador = User.objects.create_user(username='coordenador_teste', password='coordenador123', is_staff=True)
        self.coordenador.groups.add(self.group_coordenador)

        self.usuario_comum = User.objects.create_user(username='usuario_comum', password='comum123')
        self.usuario_comum.groups.add(self.group_funcionario)

        # Criar funcionários para testes de exclusão
        self.funcionario = User.objects.create_user(username='funcionario_teste', password='funcionario123')
        self.funcionario.groups.add(self.group_funcionario)

        # URL para as páginas de teste
        self.url_login = reverse('login')
        self.url_cadastro = reverse('cadastro')
        self.url_cadinfo = reverse('cadinfo')
        # self.url_excluir = reverse('excluir_funcionario', kwargs={'user_id': self.funcionario.id})

    def test_login_view(self):
        """Testa o login e redirecionamento"""
        # Testa login com usuário válido
        response = self.client.post(self.url_login, {'username': 'coordenador_teste', 'password': 'coordenador123'})
        self.assertEqual(response.status_code, 302)  # Redirecionado após login
        self.assertRedirects(response, self.url_cadinfo)  # Redireciona para a página de cadinfo

        # # Testa login com usuário inválido
        # response = self.client.post(self.url_login, {'username': 'usuario_invalido', 'password': 'senhaerrada'})
        # self.assertFormError(response, 'form', 'username', 'Este campo é obrigatório.')  # Exibe erro de login inválido

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
        self.assertEqual(response.status_code, 404)  # Verifica se ocorre um erro 404

    # def test_exclusao_funcionario(self):
    #     """Testa a exclusão de um funcionário"""
    #     # Realizar login como coordenador
    #     self.client.login(username='coordenador_teste', password='coordenador123')

    #     # Testar exclusão do funcionário
    #     response = self.client.post(self.url_excluir)
    #     self.assertEqual(User.objects.filter(username='funcionario_teste').count(), 0)  # Verifica se o funcionário foi excluído

    # def test_exclusao_funcionario_sem_permissao(self):
    #     """Testa se um usuário comum não pode excluir um funcionário"""
    #     # Realizar login como usuário comum
    #     self.client.login(username='usuario_comum', password='comum123')

    #     # Tentar excluir o funcionário
    #     response = self.client.post(self.url_excluir)
    #     self.assertEqual(User.objects.filter(username='funcionario_teste').count(), 1)  # Verifica se o funcionário não foi excluído
    #     self.assertRedirects(response, reverse('funcionarios'))  # Redireciona para outra página

    # def test_cadastro_usuario_existente(self):
    #     """Testa se exibe mensagem de erro quando o nome de usuário já existe"""
    #     # Realizar login como coordenador
    #     self.client.login(username='coordenador_teste', password='coordenador123')

    #     # Criar um usuário para testar a duplicidade
    #     User.objects.create_user(username='usuario_existente', password='senha123')

    #     response = self.client.post(self.url_cadastro, {
    #         'first_name': 'Test',
    #         'user': 'usuario_existente',
    #         'email': 'email@test.com',
    #         'password': 'senha123'
    #     })

    #     self.assertContains(response, 'Nome de usuário já existe, por favor tente novamente')

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
        self.assertEqual(User.objects.count(), 4)  # Verifica se o novo usuário foi criado
        self.assertRedirects(response, reverse('cadastro'))

    # def test_cadastro_usuario_erro(self):
    #     """Testa o tratamento de erro durante o cadastro"""
    #     # Realizar login como coordenador
    #     self.client.login(username='coordenador_teste', password='coordenador123')

    #     response = self.client.post(self.url_cadastro, {
    #         'first_name': 'Erro',
    #         'user': '',  # Nome de usuário vazio para simular erro
    #         'email': 'erro@teste.com',
    #         'password': 'senhaerro'
    #     })

    #     self.assertContains(response, 'Ocorreu um erro durante o processamento do formulário.')
