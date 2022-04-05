# Arquivo principal
# Realiza os cálculos necessários para a harmonização dos times

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