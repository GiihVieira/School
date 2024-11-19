from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from school.models import Matricula, Estudante, Curso
from school.serializers import MatriculaSerializer

class MatriculasTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.user = User.objects.get(username = 'lais')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user = self.user)
        self.estudante = Estudante.objects.get(pk = 1)
        self.curso = Curso.objects.get(pk = 1)
        self.matricula = Matricula.objects.get(pk = 1)

    def test_get_para_matricula(self):
        '''Teste de requisição GET'''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_para_uma_matricula(self):
        '''Teste de requisição GET para um Matricula'''
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_matricula = Matricula.objects.get(pk = 1)
        dados_matricula_serializados = MatriculaSerializer(instance = dados_matricula).data
        self.assertEqual(response.data, dados_matricula_serializados)

    def test_post_para_uma_matricula(self):
        '''Teste de requisição POST para um Matricula'''
        dados = {
            'estudante' : self.estudante.pk,
            'curso' : self.curso.pk,
            'periodo' : 'N'
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_para_uma_matricula(self):
        '''Teste de requisição DELETE para uma Matricula'''
        response = self.client.delete(self.url + '2/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    
    def test_put_para_uma_matricula(self):
        '''Teste de requisição PUT para uma Matricula'''
        dados = {
            'estudante' : self.estudante.pk,
            'curso' : self.curso.pk,
            'periodo' : 'N'
        }
        response = self.client.put(f'{self.url}1/', data = dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)