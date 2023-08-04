from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from stock.models import Materias
from stock.forms import MateriasForm
from stock.forms import Categoria
from django.urls import reverse
from django.http import HttpResponse


