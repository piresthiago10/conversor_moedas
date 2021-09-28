# Conversor de Moedas

API para fazer conversões entre diferentes moedas (USD, BRL, EUR, BTC, ETH) com cotações de verdade e atuais.

# Equipe:

* **Thiago Pires** - *Backend Developer*;

## Requisitos:

* Python 3.9;
* Django 3.2.7;
* Django Rest Framework 3.12.4

## Escolhas técnicas:

* Django: Permite o reaproveitamento de códigos, o que permite utilizar partes já criadas anteriormente e aplicar modificações mais pontuais.
* Django Rest Framework: Auxilia no desenvolvimento de web API's de forma simples e ágil, além de, tornar a serialização mais fácil.
* Postgres: Banco de dados com fácil integração com Django.

## Instalção:

1. Clone o projeto:
```
git clone https://github.com/piresthiago10/conversor_moedas.git
```
2. Acesse a pasta conversor_moedas e execute o arquivo:
```
run.sh
```
3. Aguarde a instalação dos containers Docker, após a instalação a API estará disponível em:
```
http://127.0.0.1:8000/, http://127.0.0.1:8000/?from=BTC&to=EUR&amount=123.45, http://127.0.0.1:8000/listagem/
```
e o Frontend em
```
http://0.0.0.0:80/
```

## Run tests:
1. Na pasta conversor_moedas execute o comando:
```
sudo docker-compose exec web python manage.py test
```
P.S: Existem poucos testes abordados sobre a api, no entando, 
não foi possível corrigir os erros de testes devido aos deadline do projeto.

## Ferramentas:

* [Docker](https://www.docker.com/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Google Chrome](https://www.google.pt/intl/pt-PT/chrome/?brand=CHBD&gclid=Cj0KCQjwn_LrBRD4ARIsAFEQFKt3kLTIsdU6a-sk3FKsxrhplkKaYNHo6Pt3aRbaEAJ3TK4fZslZmtUaAvHVEALw_wcB&gclsrc=aw)
* [Postman](https://www.postman.com/)