from django.contrib import admin
from django.urls import path, include
from school.views import EstudantesViewSet, CursosViewSet, MatriculasViewSet, MatriculasPorEstudanteViewSet, MatriculasPorCursoViewSet
from rest_framework import routers

# Define documentation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentação da API - Escola",
      default_version='v1',
      description="Documentação da API - Escola",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

# https://www.django-rest-framework.org/api-guide/routers/
router = routers.DefaultRouter()

router.register('estudantes', EstudantesViewSet, basename = 'Estudantes') # Register the new route where the first parameter refers to the URL, where the view comes from, and the name of this route.
router.register('cursos', CursosViewSet, basename = 'Cursos')
router.register('matriculas', MatriculasViewSet, basename = 'Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include(router.urls)), 
    path('estudantes/<int:pk>/matriculas', MatriculasPorEstudanteViewSet.as_view()),
    path('cursos/<int:pk>/matriculas', MatriculasPorCursoViewSet.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
