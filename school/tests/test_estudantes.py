from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Estudante
from school.serializers import EstudantesSerializer

class EstudantesTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.user = User.objects.get(username = 'lais')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user = self.user)
        self.estudante_01 = Estudante.objects.get(pk = 1)
        self.estudante_02 = Estudante.objects.get(pk = 2)

    def test_get_para_estudantes(self):
        '''Teste de requisição GET'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_para_um_estudante(self):
        '''Teste de requisição GET para um Estudante'''
        response = self.client.get(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk = 1)
        dados_estudante_serializados = EstudantesSerializer(instance = dados_estudante).data
        self.assertEqual(response.data, dados_estudante_serializados)

    def test_post_para_um_estudante(self):
        '''Teste de requisição POST para um Estudante'''
        dados = {
            'nome'            : 'teste',
            'email'           : 'teste@gmail.com',
            'cpf'             : '82271917034',
            'data_nascimento' : '2024-12-12',
            'celular'         :  '86 99999-9999'
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_para_um_estudante(self):
        '''Teste de requisição DELETE para um Estudante'''
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_para_um_estudante(self):
        '''Teste de requisição PUT para um Estudante'''
        dados = {
            'nome' : 'teste',
            'email' : 'teste@gmail.com',
            'cpf' : '61522615032',
            'data_nascimento' : '2024-12-12',
            'celular' : '88 99999-9999'
        }

        response = self.client.put(f'{self.url}1/', data = dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
