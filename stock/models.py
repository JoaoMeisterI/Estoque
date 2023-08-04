from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    class Meta:
        verbose_name = 'Category' #Singular
        verbose_name_plural = 'Categories' #Plural
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name}'


class Destino(models.Model):
    local = models.CharField(max_length=70)
    motivo = models.CharField(max_length=300)
    data = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return f'{self.local}'
    



class Materias(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=255,blank=True)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=150,blank=True)
    data = models.DateTimeField(default=timezone.now)
    preco = models.FloatField()
    fornecedor = models.CharField(max_length=40)
    garantia = models.CharField(max_length=40)
    quantidade = models.IntegerField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    destino = models.ForeignKey(
        Destino,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    def __str__(self) -> str:
        return f'{self.name}'
    

    
