from django.db import models
from django.conf import settings

class Manhwas(models.Model):
    titulo = models.TextField(default=' ', blank=False)
    genero = models.TextField (default=' ', blank=False)
    descripcion = models.TextField (default=' ', blank=False)
    autor = models.TextField (default=' ', blank=False)
    estado = models.TextField (default=' ', blank=False)
    capitulos = models.IntegerField (default=1, blank=True)
    artista = models.TextField (default=' ', blank=False)
    pais = models.TextField (default=' ', blank=True)
    clasificacion = models.TextField (default=1, blank=True)
    adaptacion = models.TextField (default="No", blank=False)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    manhwa = models.ForeignKey('manhwas.Manhwas', related_name='votes', on_delete=models.CASCADE)