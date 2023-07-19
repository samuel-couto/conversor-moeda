# Importando bibliotecas
import pandas as pd
import numpy as np
import requests as requests
import json


# Função para receber resposta do usuário
def escolha_usuario():

    # Liste todas as moedas disponíveis
    # dolar, real, iene, peso argentino
    moedas_disponiveis = ['USD', 'BRL', 'JPY', 'ARS']

    # idx será o id da moeda, iniciando por 1 como passando dentro do enumerate
    # moeda será a iteração para cada nome dentro da variável/função lista_moedas()
    print('Moedas disponíveis para consulta: ')
    print('')
    for idx, moeda in enumerate(moedas_disponiveis, 1):
        print(f"{idx} - {moeda}")

    # Escolha qual moeda origem
    print('')
    origem = int(input('Digite o número correspondente à moeda de origem de sua escolha (de): '))

    # Escolha qual moeda destino
    print('')
    destino = int(input('Digite o número correspondente à moeda de destino de sua escolha (para): '))

    # Escolha qual valor deseja converter
    print('')
    valor_converter = input('Digite o valor que deseja converter: ')
    valor_converter = round(float(valor_converter), 5)

    print('')

    # colocamos - 1 pois a lista começa com ínidce 0, então se o código escolhido for 2 tenho que tratá-lo para retornar como 1
    # retorna as moedas escolhidas
    return moedas_disponiveis[origem - 1], moedas_disponiveis[destino - 1], valor_converter


# Função para consumir API
def consome_api():

    # Chama a função que obtém as respostas do usuário
    moeda = escolha_usuario()
    moeda = list(moeda)
    moeda_origem = moeda[0]
    moeda_destino = moeda[1]

    # Requisição na API
    url = f'http://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}'
    r = requests.get(url)
    r = r.json()

    # Transformando em lista e pegando somente os valores dentro da coluna bid
    vbid = list(r.values())[0]
    vbid = vbid['bid']
    vbid = round(float(vbid), 5)

    # Valor para converter
    valor_converter = moeda[2]


    # Calculo de conversão
    valor_convertido = valor_converter * vbid

    print(f'{valor_converter} {moeda_origem} equivale à aproximadamente {valor_convertido} {moeda_destino}')

consome_api()
