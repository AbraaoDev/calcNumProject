# import mysql.connector
import matplotlib.pyplot as plt
from numpy import log as ln

import json

# ------------------------------------- ETAPA 0 (armazenando em listas)
def armazenar_em_lista(data_list):
    # Armazena as alturas, peso, e idades de todos os jogadores
    # Listas de atributos e nomes criadas, caso venha a necessitar associar os nomes aos atributos dos jogadores
    lista_alturas = []
    lista_alturas_nomes = []
    lista_pesos = []
    lista_pesos_nomes = []
    lista_idades = []
    lista_idades_nomes = []

    for i in data_list:
        for key, value in i.items():
            if key == 'ALTURA':
                lista_alturas.append(value)
            elif key == 'PESO':
                lista_pesos.append(value)
            elif key == 'IDADE':
                pass
    print("Tudo foi armazenado :)")
    return lista_alturas, lista_pesos, lista_idades

# ------------------------------------- ETAPA 1
# Calcula o IMC de cada jogador
def calc_imc(m, h):
    imc = m / h**2

    # até 4 casas decimais
    imc = round(imc, 4)

    # retorna apenas os IMCs considerados saudáveis
    if (imc >= 18.5 and imc <= 25):
        return imc
    else: 
        return "IMC não saudavel"

# Calcula o IMC médio com base nos IMCs do jogadores de um grupo (Defesa, Ataque ou Meio-Campo)
def calc_imc_medio(lista_imcs):
    y = sum(lista_imcs) / len(lista_imcs)
    return y

def delta_imc_medio(y):
    delta_y = abs(25 - y) / y
    return delta_y

def imc_aceitavel(delta_y, y):
    # onde y corresponde ao valor obtido na função imc_medio
    k0 = (1-delta_y)*y 
    k1 = (1+delta_y)*y

    # verifica se o imc está entre o intervalo: k0 <= y <= k1
    if(k0 <= y and y <= k1):
        print("IMC aceitável")
        return y
    else:
        print("Fora do intervalo")
        return 0

def calcular_altura_media(lista_alturas):
    h = sum(lista_alturas) / len(lista_alturas)
    return h

# Calcula a h0 e h1 com relação ao IMC, ver anexo do professor
def calc_h_min_h_max():
    pass

# ------------------------------------- ETAPA 2
# Cálculo da Taxa Metabólica Basal e equação de Colebrook, ver anexo do professor
def calc_tmb(idade, m, h):
    # equação proveniente do 'artigo 1' enviado pelo professor
    tmb = -0.1631 - 0.00255 * idade + 0.4721 * ln(m) + 0.2952 * ln(h)
    return tmb

# Início do programa, só vai abrir o arquivo quando sair deste loop
posicao = ""
while(posicao != "ATACANTE" or posicao != "DEFENSOR" or posicao != "MEIO-CAMPO"):
    posicao = input("Informe a posicação do jogador(ATACANTE, DEFENSOR ou MEIO-CAMPO):")
    if (posicao == "ATACANTE" or posicao == "DEFENSOR" or posicao == "MEIO-CAMPO"):
        print("Posição de campo válida.")
        break
    else:
        print("Posição de campo inválida, tente novamente.")

# abre o arquivo json referente a posição do jogador
if (posicao == "ATACANTE"):
    print("Vamos montar o time perfeito de atacantes.")
    f_atacantes = open("atacantes.json")
    data_list_atacantes = json.load(f_atacantes)

    armazenar_em_lista(data_list_atacantes)

elif (posicao == "DEFENSOR"):
    print("Vamos montar o time perfeito de defensores.")
    f_defensores = open("defensores.json")
    data_list_defensores = json.load(f_defensores)

    armazenar_em_lista(data_list_defensores)

else:
    print("Vamos montar o time perfeito de meio-campistas.")
    f_meiocampos = open("meiocampos.json")
    data_list_meiocampos = json.load(f_meiocampos)

    armazenar_em_lista(data_list_meiocampos)