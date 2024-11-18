from django.contrib import admin
from school.models import Estudante, Curso, Matricula

# Create of Display for apresentation Estudantes object
class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular') # Set the display
    list_display_links = ('id', 'nome',) # Set your links
    list_per_page = 20 # Set the maximum number of students per page to 20.
    search_fields = ('nome', 'cpf') # Set keys for search
    ordering_fields = ('nome',) # Set key for ordering

# Register the model in Admin system of Django
admin.site.register(Estudante, Estudantes) 

# Create of Display for apresentation Cursos object
class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao', 'nivel')
    list_display_links = ('id','codigo',) 
    search_fields = ('codigo',)
 
admin.site.register(Curso, Cursos) 

# Create of Display for apresentation Matriculas object
class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'estudante', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)
