from django.http import HttpResponse
import datetime

def hello(request): # primeira visão
    
    data_hota_atual = datetime.datetime.now()
    
    documento = """
    
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Minha Página Personalizada</title>
        </head>
        <body>
            <h1>Bem-vindo à Minha Página Personalizada!</h1>
            <h1 style="color:#C4c4c4">%s</h1>
            <!-- Adicione o conteúdo desejado aqui -->
        </body>
        </html>

    
    """ % data_hota_atual
    return HttpResponse(documento)


def segunda_tentativa(request, ano):
    
    
    ano_atual = int(datetime.datetime.now().strftime('%Y'))
  
    documento = "<h1> O ano inserigo %s" %(ano_atual - int(ano))
    
    return HttpResponse(documento)