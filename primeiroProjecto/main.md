````yml
name: Python CI/CD

on:
  push:
    branches:
      - main # Mude para o nome do seu branch principal

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8 # Mude para a versão Python que você está usando

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Executando testes automatizados
        run: |
          python manage.py test

      #- name: Deploy (Exemplo)
      #  if: success()
      #  run: |
      #    echo "Deploying to production..."
      # Adicione aqui os comandos necessários para implantar sua aplicação
