from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('fluxograma1/', views.fluxograma1),
    path('fluxograma2/', views.fluxograma2),
    path('fluxograma3/', views.fluxograma3),
    path('grade-horaria/', views.grade_horaria),
    path('grade-horaria-js/', views.grade_horaria_js),
    path('consulta-disciplina-1/', views.consulta_disciplina1),
    path('consulta-disciplina-2/', views.consulta_disciplina2),
]
