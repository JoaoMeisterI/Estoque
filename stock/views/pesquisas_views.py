from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from stock.models import Materias
from stock.forms import MateriasForm
from stock.forms import Categoria
from django.urls import reverse
from django.http import HttpResponse


def consulta(request):
    item = Materias.objects.all().order_by('-id')
    
    paginator = Paginator(item,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    
    
   
    categorias = Categoria.objects.all()
    
    contexto = {
        'page_obj': page_obj,
        'site_title':'Estoque - Consultas',
        'categorias': categorias,
    }
    
    return render(
        request,
        'stock/consulta.html',
        contexto

    )
    
    
    
    
def filtro(request):
    
    categoria_selecionada = ''
    
    if request.method == 'POST':
        categoria_selecionada = request.POST.get('categoria')
        
       
        
        
    
    
    
    if categoria_selecionada == 'capa':
        
        return redirect("stock:consulta")
         
    
    #Aqui tu vai colocar o valor que será filtrado na pesquisa
    #Icontains faz a relação barra filtro compara o campo name com o valor_pesquisa
    #Quando é chave estrangeira tem que colocar o campo e o nome do campo relacionado na chave estrangeira
    pesquisa = Materias.objects.all().filter(Q(categoria__name__icontains = categoria_selecionada))
    
    #Tem que retornar a tabela igual está no consulta, soq agora mais filtrado
    paginator = Paginator(pesquisa,10)
    #Mesmo esquema do paginator da consulta.py
    page_number = request.GET.get("page")
    
    page_obj = paginator.get_page(page_number)
    
    categorias = Categoria.objects.all()
    #Fazendo o filtro pela categoria
    
    #Primeiro você pega cria uma varíavel que contenha todas as categorias e faz um for no html
    
    
    contexto = {
        'page_obj': page_obj,
        'site_title': 'Consulta - Estoque',
        'categorias': categorias
    }
    
    return render(
        request,
        'stock/consulta.html',
        contexto
    )
    

  
        

        
        
        

def pesquisa(request):
    
    #Pego o valor que está sendo digitado no search
    #Get pq você vai pegar o valor do search
    valor_pesquisa = request.GET.get('q','').strip()
    
    
    #Se for vazio eu volto a página
    if valor_pesquisa == '':
        
        return redirect("stock:consulta")
    
    
    
    
    
    
   
    
    #Aqui tu vai colocar o valor que será filtrado na pesquisa
    #Icontains faz a relação barra filtro compara o campo name com o valor_pesquisa
    pesquisa = Materias.objects.all().filter(Q(name__icontains = valor_pesquisa) | Q(modelo__icontains = valor_pesquisa))
    
    #Tem que retornar a tabela igual está no consulta, soq agora mais filtrado
    paginator = Paginator(pesquisa,10)
    #Mesmo esquema do paginator da consulta.py
    page_number = request.GET.get("page")
    
    page_obj = paginator.get_page(page_number)
    
    categorias = Categoria.objects.all()
    #Fazendo o filtro pela categoria
    
    #Primeiro você pega cria uma varíavel que contenha todas as categorias e faz um for no html
    
    
    contexto = {
        'page_obj': page_obj,
        'site_title': 'Consulta - Estoque',
        'categorias': categorias
    }
    
    return render(
        request,
        'stock/consulta.html',
        contexto
    )
    

  
        
