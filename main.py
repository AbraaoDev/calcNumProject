# Arquivo principal
# Conecta ao banco de dados e coleta os registros
# Realiza os cálculos necessários para a harmonização dos times através dos registros
# ! Ainda a ser testado

import mysql.connector
from statistics import median, multimode
import matplotlib.pyplot as plt
import numpy as np

calorias_futebol = 490 

# Calcula o IMC de cada jogador
def calcular_IMC(m, h):
    imc = m / h**2

    # até 4 casas decimais
    imc = round(imc, 4)

    # retorna apenas os IMCs considerados saudáveis
    if (imc >= 18.5 and imc <= 25):
        return imc

def imc_medio():
    pass

# Calcula a massa de um jogador, dado o seu IMC e sua altura
def massa_media(imc, h):
    m = imc * h**2
    return m

# Calcula a altura média com base 
def altura_media(m_med, h_med, imc_med):
    pass
'''
m_med = media(m_j), j =1,...,nj
IMC_med = media(IMC_j), j =1,...,nj
f(h_j) = m_j/h_j**2 - IMC_j

altura media
f(h_med) = m_med/h_med**2 - IMC_med

massa_media
imc_j -> imc de cada jogador
imc_j = m_j / h_j ** 2
m_j = imc_j * h_j**2

abs(m_j - m_med) = IMC_j*(h_j - h_med)**2

(m_j - m_med)**2 = (IMC_j*(h_j - h_med)**2)**2

m_j =  m_med + IMC_j*(h_j - h_med)**2

taxa metabolica por jogador
TMB_j = 10m_j + 6.25h_j - 5idade_j + 5

desconta a altura do jogador
TMB_j = 10m_j + 6.25abs(h_j - h_med) - 5idade_j + 5
      = 10(m_j -m_med) + 6.25abs(h_j - h_med) - 5idade_j + 5

Harmonização
TMB_total = TMB_med + soma(TMB_j)

Medias das calorias
calorias gastas + os excessos
soma(cal) = media(cal) + m_j(cal)

https://gcpeixoto.github.io/METCOMP/lab-gabs/lab-04-gab.html?highlight=caloria
https://journals.plos.org/plosone/article/figure?id=10.1371/journal.pone.0103483.g004

consumo calórico 'idêntico'


Aplicar método de Newton ou Bissecção
- Ter uma linearidade na função, encontrar h_med
- m_med
- imc_med

waist = 2*pi*r
hip = 2*pi*R
waist/height = 2*pi*r/h

plotagem - waist to hips
buscar uma interseção
"Se equilibram ao ponto óptico?"
IMC = m/h**2
WH
WH + IMC = X

(h, WH)
(h,IMC)
IMC = WH
--------------------------------------------
Determinação de raízes em h
m/h**2 - IMC = f(h)


---------------------------------------------
NOVO OBJETIVO DO PROJETO
- filtrar por posição, variar entre times -> montar o melhor time
    - fixar um valor para o IMC
        - excluir quem está fora desse padrão, ou seja, um IMC diferente ao fixo
        IMC = m/h**2 + c/h
        intervalo 
        IMC = m/(h - h0)**2
        IMC = 25
        todos devem ter m kg, encontrar um valor de altura(h) ideal
    - verificar dimensões de quadril(hips) e cintura (waist)
        - plotar um gráfico para verificar se há interseção entre eles
    - defesa (n -> n)
    - meio-campo (n -> n)
    - ataque (n -> n)
    - goleiro (1 -> n)
- equilibrar parâmetros
- garantir que consumam a qtd_calorias próximas


'''
# calcula o IMC médio de um conjunto de jogadores
def calcular_imc_medio(imc):
    pass

def h_medio (h,m_med, imc_med):
    pass
    # altura média
    h_med = m_med / h**2 - imc_med

def taxa_metadbolica():
    pass

# Calcula o Gasto Calórico de cada jogador
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