"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tenis.views import lista_tenis, base, home, catalogo, ofertas, detalhes, CarrinhoView
from django.conf import settings
from dashboard import views as dashboard_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista-tenis/', lista_tenis, name='lista_tenis'),
    path('base/', base, name='base'),
    path('', home, name='home'),
    path('catalogo/', catalogo, name='catalogo'),
    path('ofertas/', ofertas, name='ofertas'),
    path('detalhes/<int:id>/', detalhes, name='detalhes'),
    path('carrinho/', CarrinhoView.as_view(), name='carrinho'),  # Exemplo de URL para o carrinho

    # Dashboard URLs 
    path('login/', dashboard_views.login_view, name='dashboard_login'),
    path('dashboard/', dashboard_views.dashboard_home, name='dashboard_home'),
    path('logout/', dashboard_views.logout_view, name='dashboard_logout'),
    path('cadastrar-tenis/', dashboard_views.cadastrar_tenis, name='cadastrar_tenis'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
