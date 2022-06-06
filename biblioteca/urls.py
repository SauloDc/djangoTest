from django.urls import path
from .views import listar, criar, atualizar, deletar

urlpatterns = [
    path("", listar, name="listar_livros"),
    path("create", criar, name="criar_livro"),
    path("update/<int:id>", atualizar, name="atualizar_livro"),
    path("delete/<int:id>", deletar, name="deletar_livro"),
]

