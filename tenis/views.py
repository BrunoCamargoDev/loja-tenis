# Create your views here.

from django.shortcuts import render, redirect
from .models import Tenis, Marca, Categoria, Usuario
from django.views import View
from django.contrib import messages

def lista_tenis(request):
    tenis = Tenis.objects.all()
    return render(request, 'lista-tenis/lista.html', {'tenis': tenis})

def base(request):
    return render(request, 'base.html')

def home(request):

    if request.method == 'POST':
        Usuario.objects.create(
            nome = request.POST.get('nome'),
            email = request.POST.get('email')
        )
        messages.success(request, 'Inscrição realizada com sucesso!')
        return redirect('home')

    tenis = Tenis.objects.all()
    destaque = Tenis.objects.filter(DestaquePrincipal=True).first()
    preco_promocional = Tenis.objects.filter(preco_promocional__isnull=False)
    return render(request, 'inicio/home.html', {'tenis': tenis, 'destaque': destaque, 'preco_promocional': preco_promocional, 'messages': messages.get_messages(request)})


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


def ofertas(request):

    tenis_promo = Tenis.objects.filter(preco_promocional__isnull=False)
    marca = request.GET.get('marca')
    categoria = request.GET.get('categoria')
    preco_max = request.GET.get('preco_max')

    if marca:
        tenis_promo = tenis_promo.filter(marca_id=marca)

    if categoria:
        tenis_promo = tenis_promo.filter(categoria_id=categoria)

    if preco_max:
        tenis_promo = tenis_promo.filter(preco__lte=preco_max)

    return render(request, 'ofertas/ofertas.html', {
        'oferta': tenis_promo,
        'marcas': Marca.objects.all(),
        'categorias': Categoria.objects.all(),
    })

def detalhes(request, id):
    tenis = Tenis.objects.get(id=id)
    return render(request, 'detalhes/detalhes.html', {'tenis': tenis})


class CarrinhoView(View):
    def get(self, request):
        tenis = Tenis.objects.all()  # Substitua por lógica para obter os itens do carrinho do usuário
            
        return render(request, 'carrinho/carrinho.html', {'tenis': tenis})