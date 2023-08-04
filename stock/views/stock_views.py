from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from stock.models import Materias
from stock.forms import MateriasForm
from django.urls import reverse

def index(request):
    

    return render(
        request,
        'stock/index.html'
    )


def cadastrar(request):

    #Retorno para essa tela, pq eu jogo isso no action
    action = reverse('stock:cadastrar')
    
    #Sé o método for post
    if request.method == 'POST':
        
        #pego o formulario  com método POST
        formulario = MateriasForm(request.POST)
        
        #Adiciono no contexto o meu formulário e minha action
        contexto = {
            'formulario': formulario,
            'action': action
        }
        
       
        
        #Se o formulário / informações registradas forem válidas 
        if formulario.is_valid():
            print("Formulário é válido")
            
            #crio um váriavel e salvo o formulario
            form = formulario.save()
            
           

            #Redireciono para minha def de atualizar para já deixar alterar algo se quiser
            #Passo a primary key gerada no cadastro do form
            
            return redirect('stock:atualizar', id_item=form.pk)
        
        #Se não cair na condição acima eu retorno essa mesma tela
        return render(
            request,
            'stock/cadastrar.html',
            contexto,
        )
    
    #Caso o Método não for post (não precisa usar Else, simplifique seu código)

    #Aqui retorna o Meu formulário de matérias só que sem método Post
    contexto = {
        'formulario': MateriasForm(),
        'action': action
    }
    
    #Renderizando e voltando as informações para não gerar erro
    
    return render(
        request,
        'stock/cadastrar.html',
        contexto
    )


def atualizar(request,id_item):
    print(id_item)
    #Pegando o Item que está sendo cadastrado
    item = get_object_or_404(Materias,pk=id_item)
    print(item)
    
    #passando a outra action que vai para o formulário
    action = reverse('stock:atualizar',args=(id_item,))
    print(action)
    
    if request.method == 'POST':
        #Passa a instancia como parâmetro isso vai indicar que o obejto já existe e é só para atualizar
        formulario = MateriasForm(request.POST,instance=item)
      
        contexto = {
            #Para passar os dados
            'formulario': formulario,
            'action': action,
        }
       
        #Verificando se um formaulário é valido
        if formulario.is_valid():
            print("Formulário é valido")
            
            form = formulario.save()
            #Para atualizar a página você usa um redirect
            #URL + PARÂMETRO
            return redirect('stock:atualizar',id_item=form.pk)
            
       
       
        return render(
            request,
            'stock/cadastrar.html',
            contexto
        )
    
    #Se não for o método post ele só retorna o formulario referenciado a instancia
    contexto = {
        'formulario': MateriasForm(instance=item)
        
    }
        
    return render(
        request,
        'stock/cadastrar.html',
        contexto
    )
