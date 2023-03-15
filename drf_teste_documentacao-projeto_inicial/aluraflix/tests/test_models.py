from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelTestCase(TestCase):
    # iniciando test
    def setUp(self):
        self.programa = Programa (
            titulo = 'Procurando ninguem em latim',
            data_lancamento ='2003-07-04'
        )

    def test_verifica_atributos_do_programa(self):
        '''
            Teste que verifica os atributos de um programa(model) com valores default
        '''
        # verificando se os valores default da model batem
        self.assertEqual(self.programa.titulo,'Procurando ninguem em latim')
        self.assertEqual(self.programa.data_lancamento,'2003-07-04')
        self.assertEqual(self.programa.tipo,'F')
        self.assertEqual(self.programa.likes,0)
        self.assertEqual(self.programa.dislikes,0)
    