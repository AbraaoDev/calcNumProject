from math import sqrt
import matplotlib.pyplot as plt
from numpy import log as ln
import random

import json

# ------------------------------------- ETAPA 0 (armazenando em listas)
def armazenar_em_lista(data_list):
    # Armazena as alturas, peso, idades e nomes de todos os jogadores
    lista_alturas = [] #0
    lista_pesos = [] #1
    lista_idades = [] #2
    lista_nomes = [] #3

    for i in data_list:
        for key, value in i.items():
            if key == 'ALTURA':
                lista_alturas.append(value)
            elif key == 'PESO':
                lista_pesos.append(value)
            elif key == 'IDADE':
                lista_idades.append(value)
            elif key == 'NOME':
                lista_nomes.append(value)
    return lista_alturas, lista_pesos, lista_idades, lista_nomes

# ------------------------------------- ETAPA 1 (Cálculo de IMCs e valores médios)
# Recebe a massa e a altura do jogador
# Retorna o imc como resultado
def calc_imc(m, h):
    imc = m / h**2

    # até 4 casas decimais
    imc = round(imc, 4)

    return imc

# Recebe a lista sequencial de todos os imc's dos jogadores
# Retorna o imc como resultado
def calc_imc_medio(lista_imcs):
    y = sum(lista_imcs) / len(lista_imcs)
    return y

# Recebe a média do IMC de todos os jogadores
# Retorna a média do IMC subtraido ao valor máximo de imc 
# aceitavel dividido pelo proprio valor maximo
def delta_imc_medio(y):
    delta_y = abs(25 - y) / y
    return delta_y

# Recebe o valor função inserida nas notas de aula que tem a função de 
# verificar se a decisão foi boa
# Recebe a média do IMC de todos os jogadores
# Retorna 1 se pertence a um intervalo aceitavel
# Retorna 0 se não pertence a um intervalo aceitavel
def imc_aceitavel(delta_y, y):
    k0 = (1 - delta_y) * y # imc minimo
    k1 = (1 + delta_y) * y # imc máximo

    return k0, k1

# Recebe a lista da altura de todos os jogadores
# Retorna a média das alturas
def calcular_altura_media(lista_alturas):
    h = sum(lista_alturas) / len(lista_alturas)
    return h

# ? Necessita revisar e aplicar um dos métodos numéricos
# parâmetros: altura média(h), delta_y(), imc_medio(y)
def calc_h_min_h_max(h, delta_y, y):
    m_barra = 25 * (h**2) 
    k0 = (1 - delta_y) * y # imc minimo
    k1 = (1 + delta_y) * y # imc máximo

    h0 = sqrt(m_barra / k0) 
    h1 = sqrt(m_barra / k1)

    return h0, h1

# ------------------------------------- ETAPA 2 (Cálculo da Taxa Metabólica Basal)
def calc_tmb(h, m, idade):
    # equação proveniente do 'artigo 1' enviado pelo professor
    tmb = -0.1631 - 0.00255 * idade + 0.4721 * ln(m) + 0.2952 * ln(h)
    tmb = round(tmb,4)
    return tmb

# para montar o time, são escolhidos 10 jogadores + 1 goleiro
def montar_time():
    pass

posicao = ""
while(posicao != "ATACANTE" or posicao != "DEFENSOR" or posicao != "MEIO-CAMPO"):
    posicao = input("Informe a posicação do jogador(ATACANTE, DEFENSOR ou MEIO-CAMPO):")
    if (posicao == "ATACANTE" or posicao == "DEFENSOR" or posicao == "MEIO-CAMPO"):
        print("Posição de campo válida.")
        break
    else:
        print("Posição de campo inválida, tente novamente.")

# Abre o arquivo .json referente a posição do jogador
if (posicao == "ATACANTE"):
    print("Vamos montar o time perfeito de atacantes.")
    f  = open("json/atacantes.json")
elif (posicao == "DEFENSOR"):
    print("Vamos montar o time perfeito de defensores.")
    f = open("json/defensores.json")
else:
    print("Vamos montar o time perfeito de meio-campistas.")
    f = open("json/meiocampos.json")

data_list = json.load(f)

# Abrindo o arquivo .json referente a posição de Goleiro
f_goleiro = open("json/goleiros.json")
data_list_goleiros = json.load(f_goleiro)

# Armazena em uma lista todos os atributos dos jogadores
# listas = [[alturas], [pesos], [idades], [nomes]]
listas = armazenar_em_lista(data_list)
lista_alturas = listas[0]
lista_pesos = listas[1]
lista_idades = listas[2]
lista_nomes = listas[3]

listas_goleiros = armazenar_em_lista(data_list_goleiros)
lista_alturas_g = listas_goleiros[0]
lista_pesos_g = listas_goleiros[1]
lista_idades_g = listas_goleiros[2]
lista_nomes_g = listas_goleiros[3]

# Para armazenar os dados dos jogadores
# nome_e_dados = [nome, m,h,i,imc]
time = []
goleiros = []

# ------------------- 1
# Referente a uma das posições informadas pelo usuário: ATACANTE, DEFENSOR e MEIO-CAMPO
imcs = []
imcs_g = []

for i in range(len(data_list)):
    imc_atual = calc_imc(lista_pesos[i], lista_alturas[i])
    nomes_e_dados = [lista_nomes[i]] 
    nomes_e_dados.append(lista_alturas[i])
    nomes_e_dados.append(lista_pesos[i])
    nomes_e_dados.append(lista_idades[i])
    nomes_e_dados.append(imc_atual)

    imcs.append(imc_atual)
    time.append(nomes_e_dados)

for i in range(len(data_list_goleiros)):
    imc_atual_g = calc_imc(lista_pesos_g[i], lista_alturas_g[i])
    nomes_e_dados_g = [lista_nomes_g[i]]
    nomes_e_dados_g.append(lista_alturas_g[i])
    nomes_e_dados_g.append(lista_pesos_g[i])
    nomes_e_dados_g.append(lista_idades_g[i])
    nomes_e_dados_g.append(imc_atual_g)

    imcs_g.append(imc_atual_g)
    goleiros.append(nomes_e_dados_g)

print(f"Foram armazenados os dados de {len(time)} de {posicao}.")
print(f"Foram armazenados os dados de {len(goleiros)} de GOLEIROS.")

# Calculo do imc_medio (y)
y = calc_imc_medio(imcs) 
y_g = calc_imc_medio(imcs_g)
print(f"O IMC médio dos {posicao} é de {y:.4f}.")
print(f"O IMC médio dos dos GOLEIROS  é de {y:.4f}.")

# Variação de IMC's
delta_y = delta_imc_medio(y)
delta_y_g = delta_imc_medio(y_g)
print(f"O valor da variação de IMCs dos {posicao} é de {delta_y}.")
print(f"O valor da variação de IMCs dos GOELIROS é de {delta_y_g}.")

# Intervalo de IMCs ceitáveis
k0,k1 = imc_aceitavel(delta_y, y)
k0_g,k1_g = imc_aceitavel(delta_y_g, y_g)
print(f"O IMC mínimo e maximo dos {posicao} é: {k0:.4f} e {k1:.4f}.")
print(f"O IMC mínimo e maximo dos GOLEIROS é: {k0_g:.4f} e {k1_g:.4f}.")

# Calcula a altura média (h)
h = calcular_altura_media(lista_alturas)
h_g = calcular_altura_media(lista_alturas_g)
print(f"A altura média dos {posicao} é: {h:.2f}m.")
print(f"A altura média dos GOLEIROS é: {h_g:.2f}m.")

# Critério para escolher o jogador

h0, h1 = calc_h_min_h_max(h,delta_y,y)
h0_g, h1_g = calc_h_min_h_max(h_g,delta_y_g,y_g)
print(f"A altura mínima e máxima dos {posicao} é: {h1:.2f}m e {h0:.2f}m.")
print(f"A altura mínima e máxima dos GOLEIROS é: {h1_g:.2f}m e {h0_g:.2f}m.")

# Selecionando jogadores com base na altura deles
sub_time = []
sub_goleiros = []
for dados in time:
    # Verifica se a altura está dentro do intervalo
    if dados[1] >= h1 and dados[1] <= h0:
        sub_time.append(dados) # adiciona linha para a nova matriz

for dados_g in goleiros:
    if dados_g[1] >= h1_g and dados_g[1] <= h0:
        sub_goleiros.append(dados_g)

print(f"Foram subselecionados {len(sub_time)}/{len(time)} {posicao}")
print(f"Foram subselecionados {len(sub_goleiros)}/{len(goleiros)} GOLEIROS.")

# ------------------- 2
# Calculando a taxa metabólica basal de todos os jogadores
taxa_metabolica = []
taxa_metabolica_g = []

for dados in sub_time:
    # como parâmetro: altura, massa e idade
    taxa = calc_tmb(dados[1], dados[2], dados[3])
    dados.append(taxa) # adiciona a taxa à lista (o valor da taxa metabolica fica armazenado na posição 5)
for dados_g in sub_goleiros:
    # como parâmetro: altura, massa e idade
    taxa_g = calc_tmb(dados_g[1], dados_g[2], dados_g[3])
    dados_g.append(taxa_g) # adiciona a taxa à lista (o valor da taxa metabolica fica armazenado na posição 5)

time_perfeito = []
jogadores_titulares = random.sample(sub_time,10) # seleciona 10 jogadores aleatório, sem repetição
goleiro_titular = random.choice(sub_goleiros) # seleciona 1 goleiro de forma aleatória

# adiciona os jogadores sorteados a lista 'time_perfeito'
time_perfeito.append(jogadores_titulares)
time_perfeito.append(goleiro_titular)

print(f"---------- O TIME PERFEITO ----------  ")
for i in range(2):
    if i == 0:
        print("--- JOGADORES TITULARES ---")
        print("Nome, altura(m), peso(kg), idade(anos), IMC, Taxa Metabólica Basal")
        for j in range(10):
            print(time_perfeito[i][j])
    else:
        print("--- GOLEIRO TITULAR ---")
        print("Nome, altura(m), peso(kg), idade(anos), IMC, Taxa Metabólica Basal")
        print(time_perfeito[i])