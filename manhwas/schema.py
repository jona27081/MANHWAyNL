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
