from django.shortcuts import render, Http404

_ALLOWED_FLUX1_PAGES = {
    "fluxograma2.html",
    "fluxograma3.html",
}

def fluxograma1_nested(request, html_file):
    # protege contra caminhos maliciosos; aceita somente nomes simples e na lista
    if ".." in html_file or "/" in html_file or html_file not in _ALLOWED_FLUX1_PAGES:
        raise Http404()
    return render(request, html_file)

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
    # arquivo: Telas/grade-horaria(javascript).html
    return render(request, 'grade-horaria(javascript).html')

def consulta_disciplina1(request):
    return render(request, 'consulta_disciplina1.html')

def consulta_disciplina2(request):
    return render(request, 'consulta_disciplina2.html')

def login_index(request):
    return render(request, 'login_index.html')

def tela_cadastro_index(request):
    return render(request, 'tela_cadastro_index.html')

def esqueci_senha(request):
    return render(request, 'esqueci-senha.html')