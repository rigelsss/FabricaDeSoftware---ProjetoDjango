from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from .models import Autor, Artigo

from .forms import AutorForm, ArtigoForm         # Vamos criar esses formulários em breve



#Lista de autores

def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'myapp/autor_list.html', {'autores': autores})



#Detalhes do autor

def autor_detail(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'myapp/autor_detail.html', {'autor':autor})




#Criação do autor

def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
    
    else:
        form = AutorForm()

    return render(request, 'myapp/autor_form.html', {'form':form})



#Atualização de autor

def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance = autor)
        if form.is_valid():
            form.save()
            return redirect('autor_list')
        
    else:
        form = AutorForm(isinstance = autor)

    return render(request, 'myapp/autor_form.html', {'form':form})


#Exclusão de autor

def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('autor_list')
    
    return render(request, 'myapp/autor_delete.html', {'autor': autor})


#Lista de artigos

def artigo_list(request):
    artigos = Artigo.objects.all()
    return render(request, 'myapp/artigo_list.html', {'artigos' : artigos})



#Detalhes do artigo

def artigo_detail(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    return render(request, 'myapp/artigo_detail.htmml', {'artigo':artigo})



#Criação de artigo

def artigo_create(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artigo_list')
    else:
        form = ArtigoForm()
    return render(request, 'myapp/artigo_form.html', {'form': form})





#Update de artigo
def artigo_update(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == 'POST':
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigo_list')
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'myapp/artigo_form.html', {'form': form})




# Exclusão de livro
def artigo_delete(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == 'POST':
        artigo.delete()
        return redirect('artigo_list')
    return render(request, 'myapp/artigo_delete.html', {'artigo': artigo})