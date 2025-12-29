from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from tenis.models import Tenis

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
    if request.method == 'POST':
        Tenis.objects.create(
            nome=request.POST['nome'],
            descricao=request.POST['descricao'],
            preco=request.POST['preco'],
            estoque=request.POST['estoque'],
            imagem=request.FILES.get('imagem'),
            DestaquePrincipal=bool(request.POST.get('DestaquePrincipal'))
        )
        return redirect('dashboard_home')

    return render(request, 'cadastro-tenis/cadastro.html')