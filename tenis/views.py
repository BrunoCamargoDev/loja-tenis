# Create your views here.

from django.shortcuts import render, redirect
from .models import Tenis, Marca, Categoria, Usuario
from django.views import View
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password

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

class LoginView(View):
    def get(self, request):
        return render(request, 'LoginCadastro/login.html')

    def post(self, request):
        email = request.POST.get('email')
        usuario = Usuario.objects.filter(email=email).first()

        if usuario:
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Usuário não encontrado. Tente novamente.')
            return redirect('login_usuario')


class CarrinhoView(View):
    def get(self, request):
        tenis = Tenis.objects.all()  # Substitua por lógica para obter os itens do carrinho do usuário
            
        return render(request, 'carrinho/carrinho.html', {'tenis': tenis})
    
class CadastroView(CreateView):
    model = Usuario
    fields = ['nome', 'email', 'senha']
    template_name = 'LoginCadastro/cadastro.html'
    success_url = reverse_lazy('login_usuario')
    
    def form_valid(self, form):
        # Este método é chamado quando o formulário é enviado com dados válidos
        
        # 1. Pegamos a instância do objeto que o formulário criou, mas ainda não salvamos no banco
        usuario = form.save(commit=False)
        
        # 2. Criptografamos a senha que veio do formulário
        usuario.senha = make_password(form.cleaned_data['senha'])
        
        messages.success(self.request, 'Cadastro realizado com sucesso! Faça login para continuar.')
        # 3. Salvamos o objeto agora com a senha segura
        usuario.save()
        
        return super().form_valid(form)

