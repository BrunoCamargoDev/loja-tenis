from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)

    def __str__(self):
        return self.nome


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Tenis(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    preco_promocional = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estoque = models.IntegerField()
    imagem = models.ImageField(upload_to='tenis-img/', null=True, blank=True)
    data_adc = models.DateTimeField(auto_now_add=True)
    DestaquePrincipal = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.DestaquePrincipal:
            Tenis.objects.filter(DestaquePrincipal=True).update(DestaquePrincipal=False)
        super().save(*args, **kwargs)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.nome
