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
    path('stock/<int:id_item>/removeItem',views.removeItem, name='removeItem'),
    
    #Views de pesquisa e filtros
    
    path('stock/consulta/',views.consulta, name='consulta'),
    path('stock/pesquisa/',views.pesquisa,name='pesquisa'),
    path('stock/filtro/',views.filtro,name='filtro'),
    path('stock/<int:id_item>/add', views.add,name='add'),
    path('stock/<int:id_item>/remove',views.remove,name='remove'),
    
    #Views de entrar para verificar o item e enviar o item
    
    path('stock/<int:id_item>/item',views.item,name='item'),
    path('stock/enviar/',views.enviar,name='enviar'),
    path('stock/historico/',views.historico,name='historico'),
    
    
]


