O python para as requisições usa duas classes 

Response HttpResponse


Visão geral rápida
O Django usa objetos de solicitação e resposta para passar o estado pelo sistema.

Quando uma página é solicitada, o Django cria um objeto que contém metadados sobre a solicitação. Em seguida, o Django carrega a visualização apropriada, passando o como o primeiro argumento para a função view. Cada modo de exibição é responsável por retornar um objeto.

Este documento explica as APIs para e objetos, que são definidos no módulo.