import mysql.connector
import matplotlib.pyplot as plt
from numpy import log as ln

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

try:
    # tenta estabelecer a conexão com o bando de dados
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='equipe3', 
        database='randomDB'
    )

    # SELECIONE os dados das colunas, DA TABELA de jogadores ONDE ...
    # É necessário editar o QUERY
    query = "SELECT column FROM tb_player WHERE" # query para selecionar os times

    cursor = connection.cursor()
    cursor.execute()

    records = cursor.fetchall()

    # Para cada linha nos registros...
    for row in records:
        pass
        # chama as funções aqui

except mysql.connector.Error as e:
    print("Erro ao ler dados da tabela ", e)

finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("Conexão encerrada.")