from rest_framework import viewsets, generics, filters
from school.models import Estudante, Curso, Matricula
from school.serializers import EstudantesSerializer, CursosSerializer, MatriculaSerializer, ListarMatriculaPorCursoSerializer, ListarMatriculasPorEstudanteSerializer, EstudantesSerializerV2
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from school.throttles import MatriculaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class EstudantesViewSet(viewsets.ModelViewSet): 
    '''
    Description of the EstudanteViewSet View
    - Endpoint for CRUD operations on students

    Sorting fields:
    - nome: allows sorting results by name.

    Search fields:
    - nome: allows searching results by name.
    - cpf: allows searching results by CPF.

    Allowed HTTP methods:
    - GET, POST, PUT, PATCH, DELETE

    Serializer class:
    - EstudanteSerializer: used for serializing and deserializing data.
    - If the accessed version is 'v2', it uses EstudanteSerializerV2.
    '''
    queryset = Estudante.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter] 
    ordering_fields = ['nome'] 
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self): 
        if self.request.version == 'v2': 
            return EstudantesSerializerV2 
        return EstudantesSerializer 

class CursosViewSet(viewsets.ModelViewSet): 
    '''
    Description of the CursoViewSet View
    - Endpoint for CRUD operations on courses

    Parameters:
    - queryset (obj): Receives the complete Curso object, already ordered by ID.
    - serializer_class (serializer): Field where the serializer for the view is defined.

    Allowed HTTP Methods:
    - GET, POST, PUT, PATCH, DELETE
    '''
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursosSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]

class MatriculasViewSet(viewsets.ModelViewSet):
    '''
    Description of the MatriculaViewSet View
    - Endpoint for CRUD operations on enrollments

    Parameters:
    - queryset (obj): Receives the complete Curso object, already ordered by ID.
    - serializer_class (serializer): Field where the serializer for the view is defined.

    Allowed HTTP Methods:
    - GET, POST

    Throttle Classes:
    - MatriculaAnonThrottle: Rate limit for anonymous users
    - UserRateThrottle: Rate limit for authenticated users
    '''
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]

class MatriculasPorEstudanteViewSet(generics.ListAPIView):
    '''
    Description of View ListaMatriculaCurso
    - List Matriculas for id of Estudantes
    Parameters:
    - pk (int): The primary identificator of object. It should be an integer.
    '''
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk']).order_by('id')
        return queryset 
    serializer_class = ListarMatriculasPorEstudanteSerializer
    
class MatriculasPorCursoViewSet(generics.ListAPIView):
    '''
    Description of View ListaMatriculaCurso
    - List Matriculas for id of Curso
    Parameters:
    - pk (int): The primary identificator of object. It should be an integer.
    '''
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListarMatriculaPorCursoSerializer
     