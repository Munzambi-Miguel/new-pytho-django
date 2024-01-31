# seu_projeto/tests.py

from django.test import TestCase
from django.urls import reverse
import datetime

class MinhaAppViewTests(TestCase):
    def test_segunda_tentativa(self):
        # Crie um cliente de teste
        response = self.client.get(reverse('calcular', args=[1992]))

        # Verifique se a resposta tem o status 200 (OK)
        self.assertEqual(response.status_code, 200)

      
      
class MinhaAppsSegundoTests(TestCase):
    
      def test_primeira_tentativa(self):
        # Crie um cliente de teste
        response = self.client.get(reverse('calcular', args=[1992]))

        # Verifique se a resposta tem o status 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        ano_atual = int(datetime.datetime.now().strftime('%Y'))
        
                
        documento = "<h1> O ano inserigo %s" %(ano_atual - 1992)
        
        
        
        self.assertContains(response, documento)
    

#     def test_segunda_tentativa(self):
#         # Crie um cliente de teste
#         response = self.client.get(reverse('nome_da_sua_url', args=[2022]))

#         # Verifique se a resposta tem o status 200 (OK)
#         self.assertEqual(response.status_code, 200)

#         # Verifique se o conteúdo da resposta é o esperado
#         ano_atual = datetime.datetime.now().strftime('%Y')
#         esperado = f"<h1> O ano inserido {int(ano_atual) - 2022}</h1>"
#         self.assertContains(response, esperado)
