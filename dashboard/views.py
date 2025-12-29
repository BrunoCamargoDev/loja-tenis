from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
        return redirect('dashboard_home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard_home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login.html')