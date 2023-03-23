from django.db import models

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

