from math import sqrt
from matplotlib.pyplot import plot
from numpy import log as ln
from numpy import linspace

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

def calc_imc_max(lista_imcs):
    y_max = max(lista_imcs)
    return y_max

# Recebe a média do IMC de todos os jogadores
# Retorna a média do IMC subtraido ao valor máximo de imc 
# aceitavel dividido pelo proprio valor maximo
def delta_imc_medio(y, y_max):
    delta_y = abs(y_max - y) / y_max
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

def calcular_massa_media(lista_pesos):
    m = sum(lista_pesos) / len(lista_pesos)
    return m

# Calcula o altura mínima por meio do método de Newton-Raphson
# Recebe como parâmetros:
    # O chute de h0 ou h1, o IMC k0 ou k1,
    # o IMC médio(removido das funções lambda), o IMC maximo, 
    # a tolerancia, nº de iterações e um valor booleano para plotagem
def newton(hx, h, kx, y, y_max, delta_y, tol, N, plotar):
    # print(f"Estimativa inicial: {hx} m.") 

    q = 1e-6 
    
    f = lambda hx: ((y_max-delta_y)*h / ((abs(h - hx)) ** 2)) -  (kx) # função 
    dnf = lambda hx: (f(hx + q) - f(hx)) / q # derivada numérica da função

    for i in range(N):
        h_x = hx - f(hx)/dnf(hx)
        e = abs(h_x-hx)/abs(h_x)
       
        if (e < tol):  # Se o erro for menor que a tolerência, para a execução
            break
        hx = h_x
    if i == N:
        print("Solução não obtida")
    
    if plotar:
        delta = 3*h_x
        dom = linspace(h_x-delta, h_x+delta, 30)
        plot(dom, f(dom), h_x, f(h_x), 'ro')
    
    return round(abs(h_x),3) # arredonda em 3 casas decimais

# ------------------------------------- ETAPA 2 (Cálculo da Taxa Metabólica Basal)
def calc_tmb(h, m, idade):
    # equação proveniente do 'artigo 1' enviado pelo professor
    tmb = -0.1631 - 0.00255 * idade + 0.4721 * ln(m) + 0.2952 * ln(h)
    tmb = round(tmb,4)
    return tmb

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
print(f"Foram armazenados os dados de {len(goleiros)} de GOLEIROS.\n")

# Calculo do imc_medio (y)
y = calc_imc_medio(imcs) 
y_g = calc_imc_medio(imcs_g)
print(f"O IMC médio dos {posicao} é de {y:.4f}.")
print(f"O IMC médio dos dos GOLEIROS  é de {y:.4f}.\n")

# Calculando o imc_max (y_max)
y_max = calc_imc_max(imcs)
y_max_g = calc_imc_max(imcs_g)
print(f"O IMC máximo dos {posicao} é de {y_max:.4f}.")
print(f"O IMC máximo dos GOLEIROS  é de {y_max_g:.4f}.\n")

# Variação de IMC's
delta_y = delta_imc_medio(y, y_max)
delta_y_g = delta_imc_medio(y_g, y_max_g)
print(f"O valor da variação de IMCs dos {posicao} é de {delta_y}.")
print(f"O valor da variação de IMCs dos GOLEIROS é de {delta_y_g}.\n")

# Intervalo de IMCs ceitáveis
k0,k1 = imc_aceitavel(delta_y, y)
k0_g,k1_g = imc_aceitavel(delta_y_g, y_g)
print(f"O IMC mínimo e maximo dos {posicao} é: {k0:.4f} e {k1:.4f}.")
print(f"O IMC mínimo e maximo dos GOLEIROS é: {k0_g:.4f} e {k1_g:.4f}\n.")

# Calcula a altura média (h)
h = calcular_altura_media(lista_alturas)
h_g = calcular_altura_media(lista_alturas_g)
print(f"A altura média dos {posicao} é: {h:.2f}m.")
print(f"A altura média dos GOLEIROS é: {h_g:.2f}m.\n")

# m = calcular_massa_media(lista_pesos)
# print(f"A massa media {m} kg.")

# Critério para escolher o jogador
# Calculando a altura mínima, chute: 1.60m
h0 = newton(1.6, h, k0, y, y_max, delta_y, 1e-3, 50, False)
h0 = h - h0
h1 = newton(2.1, h, k1, y, y_max, delta_y, 1e-3, 50, False)
h1 = h1 - (h * 0.7)
print(f"A altura mínima dos {posicao} é de: {h0:.2f} m.")
print(f"A altura maxima dos {posicao} é de: {h1:.2f} m.\n")

h0_g = newton(1.6, h_g, k0_g, y_g, y_max_g, delta_y_g, 1e-3, 50, False)
h0_g = abs(h0_g-h_g)
h1_g = newton(2.1, h_g, k1_g, y_g, y_max_g, delta_y_g, 1e-3, 50, False)
h1_g = h1_g - (h_g * 0.7)
print(f"A altura mínima dos GOLEIROS é de: {h0_g:.2f} m.")
print(f"A altura maxima dos GOLEIROS é de: {h1_g:.2f} m.\n")

# Selecionando jogadores com base na altura deles
sub_time = []
sub_goleiros = []
for dados in time:
    # Verifica se a altura está dentro do intervalo
    if dados[1] >= h0 and dados[1] <= h1:
        sub_time.append(dados) # adiciona linha para a nova matriz

for dados_g in goleiros:
    if dados_g[1] >= h0_g and dados_g[1] <= h1_g:
        sub_goleiros.append(dados_g)

print(f"Foram subselecionados {len(sub_time)}/{len(time)} {posicao}")
print(f"Foram subselecionados {len(sub_goleiros)}/{len(goleiros)} GOLEIROS.\n")

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