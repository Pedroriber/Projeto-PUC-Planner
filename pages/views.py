from django.shortcuts import render


def home(request):
    return render(request, 'home page.html')


def fluxograma1(request):
    return render(request, 'fluxograma1.html')


def fluxograma2(request):
    return render(request, 'fluxograma2.html')


def fluxograma3(request):
    return render(request, 'fluxograma3.html')


def grade_horaria(request):
    return render(request, 'grade_horaria.html')


def grade_horaria_js(request):
    return render(request, 'grade-horaria(javascript).html')


def consulta_disciplina1(request):
    return render(request, 'consulta_disciplina1.html')


def consulta_disciplina2(request):
    return render(request, 'consulta_disciplina2.html')
