from django.contrib import admin
from .models import Categoria, Marca, Tenis, Usuario


admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Tenis)
admin.site.register(Usuario)

# Register your models here.
