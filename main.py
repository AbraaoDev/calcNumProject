# Arquivo principal
# Conecta ao banco de dados e coleta os registros
# Realiza os cálculos necessários para a harmonização dos times através dos registros
# ! Ainda a ser testado

import mysql.connector
from statistics import median, multimode
import matplotlib.pyplot as plt
import numpy as np

calorias_futebol = 490 

def calcular_IMC(m, h):
    imc = m / h**2
    # até 4 casas decimais
    imc = round(imc, 4)
    # print(imc)

    # retorna apenas os IMCs considerados saudáveis
    if (imc >= 18.5 and imc <= 25):
        return imc

def gasto_calorico(idade, m):
    if (idade >= 18 and idade <= 30):
        gc = (0.063 * m + 2.896) * 239
        return gc
    elif (idade >= 31 and idade <=40): 
        gc = (0.048 * m + 3.653) * 239
        return gc

# Harmonização utilizando o método da Bissecção
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