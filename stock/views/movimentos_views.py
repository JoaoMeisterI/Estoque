from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from stock.models import Materias
from stock.models import Destino
from stock.forms import MateriasForm
from stock.forms import DestinoForm
from stock.forms import Categoria
from django.urls import reverse
from django.http import HttpResponse

#Adicionando quantidade do item
def add(request,id_item):
    item = get_object_or_404(Materias,pk=id_item)
    
    item.quantidade += 1
    
    item.save()
    
    return redirect('stock:consulta')

#Removendo quantidade do item   
def remove(request,id_item):
    item = get_object_or_404(Materias,pk=id_item)
    
    item.quantidade -= 1
    
    item.save()
    
    return redirect('stock:consulta')

def item(request,id_item):
    
    
    item = get_object_or_404(Materias,pk=id_item)
    
    contexto = {
        'item': item
        
    }
    

    return render(
        request,
        'stock/item.html',
        contexto,
    )
    
def enviar(request):
    
    
    
    if request.method == 'POST':
       
        formDestino = DestinoForm(request.POST)
        
       
        contexto = {
            'formulario': formDestino,
        }
    
        if formDestino.is_valid():
           print('formulário válido')
           form = formDestino.save()
           material = form.material.pk
           print(material) 
            

        return render(
            request,
            'stock/enviar.html',
            contexto,
        )
    
            
    
    contexto = {
            'formulario': DestinoForm(),
        }
    
    return render(
        request,
        'stock/enviar.html',
        contexto,
    )    
    
    
def historico(request):
    item = Destino.objects.all().order_by('-id')
    
    paginator = Paginator(item,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    
    
   
    categorias = Materias.objects.all()
    
    contexto = {
        'page_obj': page_obj,
        'site_title':'Estoque - Histórico',
        'categorias': categorias,
    }
    
    return render(
        request,
        'stock/historico.html',
        contexto

    )