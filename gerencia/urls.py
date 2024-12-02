from django.urls import path
from .views import inicio_gerencia, listagem_noticia,cadastrar_noticia,editar_noticia, cadastrar_categoria, editar_categoria, excluir_categoria, filtrar_categoria

app_name = 'gerencia'

urlpatterns = [
    path('', inicio_gerencia, name='gerencia_inicial'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('noticias/cadastro', cadastrar_noticia, name='cadastro_noticia'),
    path('noticias/editar/<int:id>', editar_noticia, name='editar_noticia'),
    path('cadastrar_categoria/', cadastrar_categoria, name='cadastrar_categoria'),
    path('editar_categoria/<int:id>', editar_categoria, name='editar_categoria'),
    path('excluir_categoria/<int:id>', excluir_categoria, name='excluir_categoria'),
    path('filtrar_categoria/', filtrar_categoria, name='filtrar_categoria'),
    # Add your URL patterns here
]