from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from .models import Autor, Detalhe

from .forms import AutorForm, DetalheForm         
import requests



#Lista de autores

def autor_list(request):
    fetch_autors_from_api(request)


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


#Lista de detalhes

def detalhe_list(request):
    detalhes = Detalhe.objects.all()
    return render(request, 'myapp/detalhe_list.html', {'detalhes' : detalhes})



#Detalhes do detalhe

def detalhe_detail(request, pk):
    detalhe = get_object_or_404(Detalhe, pk=pk)
    return render(request, 'myapp/detalhe_detail.htmml', {'detalhe':detalhe})



#Criação de detalhe

def detalhe_create(request):
    if request.method == 'POST':
        form = DetalheForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalhe_list')
    else:
        form = DetalheForm()
    return render(request, 'myapp/detalhe_form.html', {'form': form})





#Update de detalhe
def detalhe_update(request, pk):
    detalhe = get_object_or_404(Detalhe, pk=pk)
    if request.method == 'POST':
        form = DetalheForm(request.POST, instance=detalhe)
        if form.is_valid():
            form.save()
            return redirect('detalhe_list')
    else:
        form = DetalheForm(instance=detalhe)
    return render(request, 'myapp/detalhe_form.html', {'form': form})




# Exclusão de livro
def detalhe_delete(request, pk):
    detalhe = get_object_or_404(Detalhe, pk=pk)
    if request.method == 'POST':
        detalhe.delete()
        return redirect('detalhe_list')
    return render(request, 'myapp/detalhe_delete.html', {'detalhe': detalhe})





def fetch_autors_from_api(request):
    # Fazer a requisição para a API externa
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    print(f"Status da Requisição: {response.status_code}")  # Log do status da requisição

    if response.status_code == 200:
        users = response.json()
        print(f"Dados Recebidos: {users}")  # Log dos dados recebidos

        for user in users:
            # Verificar se o autor já existe antes de criar
            if not Autor.objects.filter(email=user['email']).exists():
                Autor.objects.create(
                    nome=user['name'],
                    email=user['email']
                )
                print(f"Autor {user['name']} criado com sucesso.")  # Log de criação do autor
            else:
                print(f"Autor {user['name']} já existe.")  # Log de autor existente

        return render(request, 'myapp/fetch_success.html', {'users': users})
    else:
        print("Falha ao buscar dados da API")  # Log de falha
        return render(request, 'myapp/fetch_fail.html', {'error': response.status_code})
