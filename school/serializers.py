from rest_framework import serializers
from school.models import Estudante, Curso, Matricula
from school.validators import cpf_invalido, nome_invalido, celular_invalido


class EstudantesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Estudante 
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    def validate(self, data):
        if cpf_invalido(data['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ser um valor válido!'})
        if nome_invalido(data['nome']):
            raise serializers.ValidationError({'nome':'O nome só pode ter letras!'})
        if celular_invalido(data['celular']):
            raise serializers.ValidationError({'celular':'O celular dever seguir o modelo: 99 99999-9999'})
        return data

class EstudantesSerializerV2(serializers.ModelSerializer): 
    class Meta:
        model = Estudante 
        fields = ['id', 'nome', 'email', 'celular']

class CursosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Curso 
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Matricula 
        fields = '__all__' 

class ListarMatriculasPorEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source = 'curso.descricao') 
    periodo = serializers.SerializerMethodField() 
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListarMatriculaPorCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta: 
        model = Matricula
        fields = ['estudante_nome']
