import graphene

import manhwas.schema


class Query(manhwas.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)