
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fluxograma1/', views.fluxograma1, name='fluxograma1'),
    # rota adicional para aceitar caminhos como /fluxograma1/fluxograma2.html
    path('fluxograma1/<str:html_file>', views.fluxograma1_nested, name='fluxograma1_nested'),
    path('fluxograma2/', views.fluxograma2, name='fluxograma2'),
    path('fluxograma3/', views.fluxograma3, name='fluxograma3'),
    path('grade-horaria/', views.grade_horaria, name='grade_horaria'),
    path('grade-horaria-js/', views.grade_horaria_js, name='grade_horaria_js'),
    path('consulta-disciplina-1/', views.consulta_disciplina1, name='consulta_disciplina1'),
    path('consulta-disciplina-2/', views.consulta_disciplina2, name='consulta_disciplina2'),
    path('login/', views.login_index, name='login'),
    path('cadastro/', views.tela_cadastro_index, name='tela_cadastro_index'),
    path('esqueci-senha/', views.esqueci_senha, name='esqueci_senha'),
]