import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType
from manhwas.models import Manhwas, Vote
from graphql import GraphQLError
from django.db.models import Q


class ManhwasType(DjangoObjectType):
    class Meta:
        model = Manhwas
    # ...code

# Add after the LinkType


class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(graphene.ObjectType):
    manhwas = graphene.List(ManhwasType, search=graphene.String())
    votes = graphene.List(VoteType)

    def resolve_manhwas(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(titulo__icontains=search) |
                Q(descripcion__icontains=search)
            )
            return Manhwas.objects.filter(filter)
        
        return Manhwas.objects.all()

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()


# 1
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
    posted_by = graphene.Field(UserType)

    # 2
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

    # 3
    def mutate(self, info, titulo, genero, descripcion, autor, estado, capitulos, artista, pais, clasificacion, adaptacion):
        user = info.context.user or None
        manhwas = Manhwas(
            titulo=titulo,
            genero=genero,
            descripcion=descripcion,
            autor=autor,
            estado=estado,
            capitulos=capitulos,
            artista=artista,
            pais=pais,
            clasificacion=clasificacion,
            adaptacion=adaptacion,
            posted_by=user,
        )
        manhwas.save()

        return CreateManhwas(
            id=manhwas.id,
            titulo=manhwas.titulo,
            genero=manhwas.genero,
            descripcion=manhwas.descripcion,
            autor=manhwas.autor,
            estado=manhwas.estado,
            capitulos=manhwas.capitulos,
            artista=manhwas.artista,
            pais=manhwas.pais,
            clasificacion=manhwas.clasificacion,
            adaptacion=adaptacion,
            posted_by=manhwas.posted_by
        )

# Add the CreateVote mutation


class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    manhwas = graphene.Field(ManhwasType)

    class Arguments:
        m_id = graphene.Int()

    def mutate(self, info, m_id):
        user = info.context.user
        if user.is_anonymous:
            # 1
            raise GraphQLError('You must be logged to vote!')

        manhwas = Manhwas.objects.filter(id=m_id).first()
        if not manhwas:
            raise Exception('Invalid Link!')

        Vote.objects.create(
            user=user,
            manhwa=manhwas,
        )

        return CreateVote(user=user, manhwas=manhwas)


# ...code
class Mutation(graphene.ObjectType):
    create_manhwas = CreateManhwas.Field()
    create_vote = CreateVote.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
