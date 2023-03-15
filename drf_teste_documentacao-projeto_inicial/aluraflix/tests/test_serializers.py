from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializerTestCase(TestCase):
    # iniciando teste
    def setUp(self):
        self.programa = Programa (
            titulo = 'Procurando ninguem em latim',
            data_lancamento ='2003-07-04',
            tipo = 'F',
            likes = 2340,
            dislikes = 40
        )
        # testando serializer 
        # passando valores para serializer
        self.serializer = ProgramaSerializer(instance= self.programa)
        # verificando se os campos serializados são os campos que devem ser serializados
    
    def test_verifica_campos_serializados(self):
        '''
            Teste que verifica os campos que estão sendo serializados
        '''
        # pegando todos os campos do serializer e atribuindo a uma variável
        data = self.serializer.data
        # verificando se o serializer possui os seguintes campos
        # set(data.keys()) pega o nome dos campos da variavel data
        self.assertEqual(set(data.keys()),set(['titulo', 'tipo', 'data_lancamento', 'likes']))
    
    def test_verifica_conteudo_dos_campos_serializados(self):
        '''
            Teste que verifica o conteudos dos campos serializados
        '''
        # pegando os dados do serializer
        data = self.serializer.data
        # testando se os valores dos campos  são iguais ao do setUp
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['likes'], self.programa.likes)
        