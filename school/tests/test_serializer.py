from django.test import TestCase
from school.models import Estudante, Curso, Matricula
from school.serializers import EstudantesSerializer, CursosSerializer, MatriculaSerializer

class EstudantesSerializerTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome = 'Teste Estudante',
            email = 'testeestudante@gmail.com',
            cpf = '47328482060',
            data_nascimento = '2024-11-19',
            celular = '86 99999-9999',
        )
        self.serializer_estudante = EstudantesSerializer(instance = self.estudante)

    def test_verifica_campos_serializados_de_estudante(self):
        '''Teste que verifica os campos que estão sendo serializados de Estudante'''
        dados = self.serializer_estudante.data
        self.assertEqual(set(dados.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']))

    def test_verifica_conteudo_dos_campos_serializados_de_estudante(self):
        '''Teste que verifica os conteudos dos campos que estão sendo serializados de Estudante'''
        dados = self.serializer_estudante.data
        self.assertEqual(dados['nome'], self.estudante.nome)
        self.assertEqual(dados['email'], self.estudante.email)
        self.assertEqual(dados['cpf'], self.estudante.cpf)
        self.assertEqual(dados['data_nascimento'], self.estudante.data_nascimento)
        self.assertEqual(dados['celular'], self.estudante.celular)


class CursosSerializerTestCase(TestCase):
    def setUp(self):
        self.curso = Curso(
            codigo = 'CPOO01',
            descricao = 'Curso de Programação Orientada a Objetos 1',
            nivel = 'A',
        )
        self.serializer_curso = CursosSerializer(instance = self.curso)

    def test_verifica_campos_serializados_de_curso(self):
        '''Teste que verifica os campos que estão sendo serializados de Curso'''
        dados = self.serializer_curso.data
        self.assertEqual(set(dados.keys()), set(['id', 'codigo', 'descricao', 'nivel']))

    def test_verifica_conteudo_dos_campos_serializados_de_curso(self):
        '''Teste que verifica o conteudo dos campos que estão sendo serializados de Curso'''
        dados = self.serializer_curso.data
        self.assertEqual(dados['codigo'], self.curso.codigo)
        self.assertEqual(dados['descricao'], self.curso.descricao)
        self.assertEqual(dados['nivel'], self.curso.nivel)
       