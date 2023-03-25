from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        # o -list lista os endpoinst(rotas) de programas
        self.list_url = reverse('programas-list')
        # criando usuário para teste
        self.user = User.objects.create_user(
            'c3po',
            password= '123456'
        )
    
    def test_autenticacao_user_com_credenciais_corretas(self):
        '''
            teste que verifica a autentticao de um user com as credenciais corretas
        '''
        user = authenticate(username = 'c3po',  password= '123456')
        # verificando  se o user está com valores e autenticado
        self.assertTrue(user is not None) and user.is_authenticated
    
    def test_requisicao_get_nao_autorizada(self):
        '''
            teste que verifica uma requisição GET não autorizado 
        '''
        # fazendo uma requisição do tipo get
        response =self.client.get(self.list_url)
        # se o código de status é igual a 401(não autorizado)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    
    def test_autenticacao_de_user_com_username_incorreto(self):
        '''
            Teste que verifica autenticação de um user com username incorreto
        '''
        # errando o nick 
        user = authenticate(username = 'c3pp',  password= '123456')
        # verificando  se o user está o username errado
        self.assertFalse(user is not None) and user.is_authenticated
    
    def test_autenticacao_de_user_com_password_incorreto(self):
        '''
            Teste que verifica autenticação de um user com username incorreto
        '''
        # errando a senha 
        user = authenticate(username = 'c3po',  password= '1234567')
        # verificando  se o user está o username errado
        self.assertFalse(user is not None) and user.is_authenticated

    
    def test_requisicao_get_com_user_autenticado(self):
        '''
            Teste que verifica uma requisição GET de um user autenticado 
        '''
        # fazendo requisição
        self.client.force_authenticate(self.user)
        # fazendo requisição get
        response =self.client.get(self.list_url)
        # verificando se deu certo a requisição do usuário logado
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    