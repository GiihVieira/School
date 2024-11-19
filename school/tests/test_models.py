from django.test import TestCase
from school.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste Estudante',
            email = 'testeestudante@gmail.com',
            cpf = '47328482060',
            data_nascimento = '2024-11-19',
            celular = '86 99999-9999',
        )

    def test_verifica_atributos_estudante(self):
        '''Teste que verifica os atributos do modelo de Estudante'''
        self.assertEqual(self.estudante.nome, 'Teste Estudante')
        self.assertEqual(self.estudante.email, 'testeestudante@gmail.com')
        self.assertEqual(self.estudante.cpf, '47328482060')
        self.assertEqual(self.estudante.data_nascimento, '2024-11-19')
        self.assertEqual(self.estudante.celular, '86 99999-9999')


class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'CPOO01',
            descricao = 'Curso de Programação Orientada a Objetos 1',
            nivel = 'A',
        )

    def test_verifica_atributos_curso(self):
        '''Teste que verifica os atributos do modelo de Curso'''
        self.assertEqual(self.curso.codigo, 'CPOO01')
        self.assertEqual(self.curso.descricao, 'Curso de Programação Orientada a Objetos 1')
        self.assertEqual(self.curso.nivel, 'A')


class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste Estudante',
            email = 'testeestudante@gmail.com',
            cpf = '47328482060',
            data_nascimento = '2024-11-19',
            celular = '86 99999-9999',
        )
        self.curso = Curso.objects.create(
            codigo ='CPOO01',
            descricao = 'Curso de Programação Orientada a Objetos 1',
            nivel = 'A',
        )
        self.matricula = Matricula.objects.create(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'N',
        )

    def test_verifica_atributos_matricula(self):
        self.assertEqual(self.matricula.estudante, self.estudante)
        self.assertEqual(self.matricula.curso, self.curso)
        self.assertEqual(self.matricula.periodo, 'N')
