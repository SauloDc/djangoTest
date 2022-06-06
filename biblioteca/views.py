from django.shortcuts import redirect, render
from .models import Livro
from .forms import LivroForm

def listar(request):
    lista = Livro.objects.all()
    return render(request, 'listagem.html', {'lista': lista})

def criar(request):
    form = LivroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar_livros')
    return render(request, 'livros-create.html', {'form': form})

def atualizar(request, id):
    livro = Livro.objects.get(id=id)
    form = LivroForm(request.POST or None, request.FILES or None, instance=livro)
    if form.is_valid():
            form.save()
            return redirect('listar_livros')
    return render(request, 'livros-edit.html', {'form': form, 'livro': livro})

def deletar(request, id):
    livro = Livro.objects.get(id=id)

    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request, 'livro-delete.html', {'livro': livro})
