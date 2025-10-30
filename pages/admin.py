from django.contrib import admin
from .models import Disciplina, Curso, Professor, Turma

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'creditos', 'semestre', 'obrigatoria')
    search_fields = ('codigo', 'nome')
    filter_horizontal = ('prerequisitos',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'creditos_totais')
    filter_horizontal = ('disciplinas',)

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    filter_horizontal = ('disciplinas',)

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'codigo', 'professor', 'ano', 'semestre', 'capacidade')
    list_filter = ('ano', 'semestre')