# Arquivo principal responsável pela Harmonização
# ! Ainda é necessário testar a conexão

import mysql.connector
import matplotlib.pyplot as plt
from numpy import log as ln

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
    imc_medio = sum(lista_imcs) / len(lista_imcs)
    return imc_medio

# Cálculo da Taxa Metabólica Basal
def calc_tmb(idade, m, h):
    # equação proveniente do 'artigo 1' enviado pelo professor
    tmb = -0.1631 - 0.00255 * idade + 0.4721 * ln(m) + 0.2952 * ln(h)
    return tmb

# Harmonização utilizando o método da equação de Cole, por não ser linear
def harmonizar():
    pass

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