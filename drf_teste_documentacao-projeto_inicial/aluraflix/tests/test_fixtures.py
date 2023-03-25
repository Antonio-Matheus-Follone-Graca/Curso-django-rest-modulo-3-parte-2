from django.test import TestCase
from aluraflix.models import Programa

class FixturesDataTestCase(TestCase):
    # testando fixtures
    # falando aonde está o arquivo de fixtures
    fixtures = ['programas_iniciais']

    def test_verifica_carregamento_da_fixtures(self):
        programa_bizarro = Programa.objects.get(pk = 1)
        todos_os_programas = Programa.objects.all()
        self.assertEqual(programa_bizarro.titulo,"Coisas bizarras")
        self.assertEqual(len(todos_os_programas),9)