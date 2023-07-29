from django.urls import path
from stock import views
from django.contrib import admin



urlpatterns = [
    
    #URL inicial
    path('',views.index, name='index'),
    
    path('admin/', admin.site.urls),
    
]

