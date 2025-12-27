# Create your views here.

from django.shortcuts import render
from .models import Tenis, Marca, Categoria

def lista_tenis(request):
    tenis = Tenis.objects.all()
    return render(request, 'lista-tenis/lista.html', {'tenis': tenis})

def base(request):
    return render(request, 'base.html')

def home(request):
    tenis = Tenis.objects.all()
    return render(request, 'inicio/home.html', {'tenis': tenis})


def catalogo(request):
    tenis = Tenis.objects.all()

    marca = request.GET.get('marca')
    categoria = request.GET.get('categoria')
    preco_max = request.GET.get('preco_max')

    if marca:
        tenis = tenis.filter(marca_id=marca)

    if categoria:
        tenis = tenis.filter(categoria_id=categoria)

    if preco_max:
        tenis = tenis.filter(preco__lte=preco_max)

    return render(request, 'catalogo/catalogo.html', {
        'tenis': tenis,
        'marcas': Marca.objects.all(),
        'categorias': Categoria.objects.all(),
    })