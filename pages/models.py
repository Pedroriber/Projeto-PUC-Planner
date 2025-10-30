from django.db import models

class Disciplina(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=200)
    creditos = models.PositiveSmallIntegerField()
    descricao = models.TextField(blank=True)
    semestre = models.PositiveSmallIntegerField(null=True, blank=True)
    obrigatoria = models.BooleanField(default=True)
    prerequisitos = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='dependentes')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['codigo']
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class Curso(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=200)
    creditos_totais = models.PositiveIntegerField()
    disciplinas = models.ManyToManyField(Disciplina, blank=True, related_name='cursos')

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class Professor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    disciplinas = models.ManyToManyField(Disciplina, blank=True, related_name='professores')

    def __str__(self):
        return self.nome


class Turma(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='turmas')
    codigo = models.CharField(max_length=50, blank=True)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True, related_name='turmas')
    ano = models.PositiveSmallIntegerField()
    semestre = models.PositiveSmallIntegerField()
    capacidade = models.PositiveIntegerField(default=30)

    class Meta:
        unique_together = ('disciplina', 'ano', 'semestre', 'codigo')
        ordering = ['-ano', '-semestre', 'disciplina']

    def __str__(self):
        if self.codigo:
            return f"{self.disciplina.codigo} - {self.codigo} ({self.ano}.{self.semestre})"
        return f"{self.disciplina.codigo} ({self.ano}.{self.semestre})"