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

CREATE_MANHWA_MUTATION = '''
mutation createManhwas($titulo: String, $genero: String, $descripcion: String, $autor: String, $estado: String, $capitulos: Int, $artista: String, $pais: String, $clasificacion: String, $adaptacion: String) {
    createManhwas(titulo: $titulo, genero: $genero, descripcion: $descripcion, autor: $autor, estado: $estado, capitulos: $capitulos, artista: $artista, pais: $pais, clasificacion: $clasificacion, adaptacion: $adaptacion) {
      titulo
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
        # print(content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print("query manhwas results ")
        print(content)
        assert len(content['data']['manhwas']) == 2


    def test_createManhwa_mutation(self):

        response = self.query(
            CREATE_MANHWA_MUTATION,
            variables={'titulo': 'The God of High School', 'genero': 'Acción, Aventura, Comedia, Fantasía',
                      'descripcion': 'Jin Mo-Ri, un estudiante de preparatoria y experto en artes marciales', 'autor': 'Park Yong-Je',
                      'estado': 'Completo', 'capitulos': 517, 'artista': 'Park Yong-Je', 'pais': 'Corea del Sur',
                      'clasificacion': 'Mayores de 14 años', 'adaptacion': 'Webtoon'}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual( 
            {"createManhwas": {"titulo": "The God of High School"}}, content['data'])
