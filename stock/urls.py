from django.urls import path
from stock import views
from django.contrib import admin

app_name = 'stock'

urlpatterns = [
    
    #URL inicial
    #Views CRUD (sem read)
    path('',views.index, name='index'),
    path('stock/cadastrar/',views.cadastrar, name='cadastrar'),
    path('stock/<int:id_item>/atualizar',views.atualizar, name='atualizar'),
    
    #Views de pesquisa e filtros
    
    path('stock/consulta/',views.consulta, name='consulta'),
    path('stock/pesquisa/',views.pesquisa,name='pesquisa'),
    path('stock/filtro',views.filtro,name='filtro'),
]

