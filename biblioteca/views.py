from django.shortcuts import render
from .models import Livro

def listar(request):
    lista = Livro.objects.all()
    return render(request, 'listagem.html', {'lista': lista})

def editar(request, id):
    lista = Livro.objects.all()
    return render(request, 'editar.html', {'lista': lista})
