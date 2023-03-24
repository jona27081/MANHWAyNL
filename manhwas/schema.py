import graphene
from graphene_django import DjangoObjectType

from .models import Manhwas
from manhwas import models


class ManhwasType(DjangoObjectType):
    class Meta:
        model = Manhwas


class Query(graphene.ObjectType):
    manhwas = graphene.List(ManhwasType)

    def resolve_manhwas(self, info, **kwargs):
        return Manhwas.objects.all()
    

#1
class CreateManhwas(graphene.Mutation):
    id = graphene.Int()
    titulo = graphene.String()
    genero = graphene.String()
    descripcion = graphene.String()
    autor = graphene.String()
    estado = graphene.String()
    capitulos = graphene.Int()
    artista = graphene.String()
    pais = graphene.String()
    clasificacion = graphene.String()
    adaptacion = graphene.String()

    #2
    class Arguments:
        titulo = graphene.String()
        genero = graphene.String()
        descripcion = graphene.String()
        autor = graphene.String()
        estado = graphene.String()
        capitulos = graphene.Int()
        artista = graphene.String()
        pais = graphene.String()
        clasificacion = graphene.String()
        adaptacion = graphene.String()

    #3
    def mutate(self, info, titulo, genero, descripcion, autor, estado, capitulos, artista, pais, clasificacion, adaptacion):
        manhwas = Manhwas(
                          titulo=titulo,
                          genero =genero,
                          descripcion=descripcion,
                          autor=autor,
                          estado=estado,
                          capitulos=capitulos,
                          artista=artista,
                          pais=pais,
                          clasificacion=clasificacion,
                          adaptacion=adaptacion
                          )
        manhwas.save()

        return CreateManhwas(
            id=manhwas.id,
            titulo=manhwas.titulo,
            genero =manhwas.genero,
            descripcion=manhwas.descripcion,
            autor=manhwas.autor,
            estado=manhwas.estado,
            capitulos=manhwas.capitulos,
            artista=manhwas.artista,
            pais=manhwas.pais,
            clasificacion=manhwas.clasificacion,
            adaptacion=adaptacion
        )

#4
class Mutation(graphene.ObjectType):
    create_manhwas = CreateManhwas.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)