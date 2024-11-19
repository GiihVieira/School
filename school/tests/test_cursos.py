from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Curso
from school.serializers import CursosSerializer

class CursosTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.user = User.objects.get(username = 'lais')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user = self.user)
        self.curso_01 = Curso.objects.get(pk = 1)
        self.curso_02 = Curso.objects.get(pk = 2)

    def test_get_para_curso(self):
        '''Teste de requisição GET'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_para_um_curso(self):
        '''Teste de requisição GET para um Curso'''
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk = 1)
        dados_curso_serializados = CursosSerializer(instance = dados_curso).data
        self.assertEqual(response.data, dados_curso_serializados)

    def test_post_para_um_curso(self):
        '''Teste de requisição POST para um Curso'''
        dados = {
            'codigo'    : 'CF01',
            'descricao' : 'Curso de Fork 01',
            'nivel'     : 'A'            
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_para_um_curso(self):
        '''Teste de requisição DELETE para um Curso'''
        response = self.client.delete(self.url + '2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_para_um_curso(self):
        '''Teste de requisição PUT para um Curso'''
        dados = {
            'codigo'    : 'CF01',
            'descricao' : 'Curso de Fork 01',
            'nivel'     : 'A'  
        }
        response = self.client.put(f'{self.url}1/', data = dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)