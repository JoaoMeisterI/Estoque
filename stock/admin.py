from django.contrib import admin
from stock import models


# Register your models here.


@admin.register(models.Materias)
class MateriasAdmin(admin.ModelAdmin):
    list_display = 'name','modelo','data','categoria','destino',
    
    

@admin.register(models.Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = 'local','motivo','data',
    


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = 'name',
    
    
    
