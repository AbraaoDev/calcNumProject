import matplotlib.pyplot as plt
import json

from numpy import log as ln

# ---------------- CRIANDO AS FUNÇÕES ---------------- #

# -----------------------------------------------------------
# Recebe a lista pura em json
# Retorna uma lista sequencial contendo os dados SEPARADOS
# de uma mesma propriedade de todos os jogadores
def Armazenar_em_lista(data_list):
    # Armazena as alturas, peso, idades e nomes de todos os jogadores
    lista_alturas = [] #0
    lista_pesos = [] #1
    lista_idades = [] #2
    lista_nomes = [] #3

	#Dentro desse for, ele estará verificando se a chave equivale a determinada propriedade do jogador
	# se sim, insere no final da lista o valor
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

# -----------------------------------------------------------
# Recebe a massa e a altura do jogador
# Retorna o imc como resultado
def Calc_imc(m, h):
	#IMC = masse / altura^2
    imc = m / (h*h)
    imc = round(imc, 4) #Arredonda para até 4 casas decimais após a virgula

    return imc

# -----------------------------------------------------------
# Recebe a lista sequencial de todos os imc's dos jogadores
# Retorna o imc como resultado
def Calc_imc_medio(lista_imcs):
    y = sum(lista_imcs) / len(lista_imcs)
    return y

# -----------------------------------------------------------
# Recebe a média do IMC de todos os jogadores
# Retorna a média do IMC subtraido ao valor máximo de imc 
# aceitavel dividido pelo proprio valor maximo
def Delta_imc_medio(y):
    delta_y = abs(25 - y) / 25
    return delta_y

# -----------------------------------------------------------
# Recebe o valor função inserida nas notas de aula que tem a função de 
# verificar se a decisão foi boa
# Recebe a média do IMC de todos os jogadores
# Retorna 1 se pertence a um intervalo aceitavel
# Retorna 0 se não pertence a um intervalo aceitavel
def Imc_aceitavel(delta_y, y):
    k0 = (1-delta_y)*y 
    k1 = (1+delta_y)*y
    if(k0 <= y and y <= k1):
        #print("IMC aceitável")
        return 1
    else:
        #print("Fora do intervalo")
        return 0

# -----------------------------------------------------------
# Recebe a lista da altura de todos os jogadores
# Retorna a média das alturas
def Calcula_altura_media(lista_alturas):
    h = sum(lista_alturas) / len(lista_alturas) # h = (soma da lista das alturas) / (comprimento da lista, logo, quantos jogadores ela tem)
    return h


# -----------------------------------------------------------
# Recebe
# Retorna
#def Calc_h_min_h_max():
    #Em desenvolvimento

# -----------------------------------------------------------
# Recebe
# Retorna

# ---------------- EXECUÇÃO DO PROJETO ---------------- #

#Informa a posição desejada
posicao = "DESCONHECIDA"
while(posicao == "DESCONHECIDA"):
    posicao = input("Informe a posicação do jogador(ATACANTE, DEFENSOR ou MEIO-CAMPO):")
    if (posicao == "ATACANTE" or posicao == "DEFENSOR" or posicao == "MEIO-CAMPO"):
        break
    else:
        print("Posição de campo inválida, tente novamente.")
        posicao = "DESCONHECIDA"

#Monta os melhores jogadores daquela posição desejada
print("Vamos montar o time perfeito de ", {posicao})
if(posicao == "ATACANTE"):
    f = open("json/atacantes.json")
elif(posicao == "MEIO-CAMPO"):
    f = open("json/meiocampos.json")
elif(posicao == "DEFENSOR"):
    f = open("json/defensores.json")
data_list = json.load(f)

# Armazena uma lista de 4 colunos e N linhas (sendo N a quantidade de jogadores presente na base de dados)
listas = Armazenar_em_lista(data_list)
lista_alturas = listas[0]
lista_pesos = listas[1]
lista_idades = listas[2]
lista_nomes = listas[3]

# Declaração das várias armazenadoras de propriedades de um time e um IMC deles
time = []
imcs = []

#Cria uma nova lista contendo as informações dos jogadores e o IMC de cada um deles
for i in range(len(data_list)):
    # 0 0 
    imc_atual = Calc_imc(lista_pesos[i], lista_alturas[i])
    nomes_e_dados = [lista_nomes[i]]
    nomes_e_dados.append(lista_alturas[i])
    nomes_e_dados.append(lista_pesos[i])
    nomes_e_dados.append(lista_idades[i])
    nomes_e_dados.append(imc_atual)

    imcs.append(imc_atual)
    time.append(nomes_e_dados)

y = Calc_imc_medio(imcs)
delta_y = Delta_imc_medio(y)

for i in range(len(data_list)):
    temp_var = Imc_aceitavel(delta_y, y)
    if(temp_var == 0):
        print("IMC fora da faixa aceitavel")
nomes_e_dados.append(temp_var)

altura_media = 0
for i in range(len(data_list)):
    altura_media = altura_media + lista_alturas[i]
altura_media = altura_media / len(data_list)
print("A altura media vale", {altura_media})

print("FIM DO CODIGO")