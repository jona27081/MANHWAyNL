from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from manhwas.schema import schema
from manhwas.models import Manhwas

MANHWAS_QUERY = '''
{
  manhwas{
    id,
    titulo,
    genero,
    descripcion,
    autor,
    estado,
    capitulos,
    artista,
    pais,
    clasificacion,
    adaptacion,
  }
}
'''

class ManhwaTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.manhwa1 = mixer.blend(Manhwas)
        self.manhwa2 = mixer.blend(Manhwas)

    def test_manhwas_query(self):
        response = self.query(
            MANHWAS_QUERY,
        )


        content = json.loads(response.content)
        #print(content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print ("query manhwas results ")
        print (content)
        assert len(content['data']['manhwas']) == 2


