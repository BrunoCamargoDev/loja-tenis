from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from tenis.models import Tenis, Marca, Categoria
from decimal import Decimal

# Create your views here.

def dashboard_home(request):
    return render(request, 'home.html')


# Função logout
def logout_view(request):
    logout(request)
    return redirect('dashboard_login')

# Função login
def login_view(request):
    if request.user.is_staff:
        return redirect('cadastrar_tenis') # tava dashboard_home

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('cadastrar_tenis') # tava dashboard_home
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login/login.html')


def cadastrar_tenis(request):
    marcas = Marca.objects.all()
    categorias = Categoria.objects.all()

    if request.method == 'POST':

        # tratar preco_promocional
        preco_prom_input = request.POST.get('preco_promocional')
        preco_promocional = Decimal(preco_prom_input) if preco_prom_input else None

        # tratar destaque
        destaque = bool(request.POST.get('DestaquePrincipal'))

        Tenis.objects.create(
            nome=request.POST.get('nome'),
            descricao=request.POST.get('descricao'),
            preco=request.POST.get('preco'),
            preco_promocional=preco_promocional,
            estoque=request.POST.get('estoque') or 0,  # garante que não seja vazio
            categoria_id=request.POST.get('categoria') or None,
            marca_id=request.POST.get('marca') or None,
            imagem=request.FILES.get('imagem'),
            DestaquePrincipal=destaque
        )

        return redirect('dashboard_home')

    return render(request, 'cadastro-tenis/cadastro.html', {
        'marcas': marcas,
        'categorias': categorias
    })