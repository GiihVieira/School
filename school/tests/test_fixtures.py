from django.test import TestCase
from school.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_fixtures(self):
        '''Teste que verifica o carregamento da Fixtures'''
        estudante = Estudante.objects.get(cpf = '93277294390')
        curso = Curso.objects.get(pk = 1)
        self.assertEqual(estudante.celular, '34 94465-7330')
        self.assertEqual(curso.codigo, 'CPOO1')

