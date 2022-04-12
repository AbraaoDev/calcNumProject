import pandas as pd
from flask import Flask, jsonify, render_template

import json

app = Flask(__name__)
app.config["DEBUG"] = True

# Rota raiz
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    # return "<h1>Bola Na Rede -  Equipe 3</h1>"

# Rota para exibir a equipe do projeto
@app.route('/equipe', methods=['GET'])
def equipe():
    return render_template('equipe.html')

# Rota de filtragem
# ! Ainda em implementação
@app.route('/filtrar_time', methods=['GET'])
def teste():
    df = pd.read_csv('BrasileiraoSerieA.csv')
    json_str = df.to_json(orient='records')

    # Vai ter um forms :D
    time_selecionado = df[df['TIME'] == "AMERICA-MG"]
    soma = df['ALTURA'].sum()
    print(f"A soma das alturas é de: {soma}")
    print(time_selecionado)
    print(type(soma))
    response = {'Alturas': soma}
    print(type(response))

    return response

# Retorna todo o dataframe no formato json
@app.route('/listar_all', methods=['GET'])
def listar_all():
    df = pd.read_csv('BrasileiraoSerieA.csv')
    df_dict = df.to_dict(orient='records') # ordena o dataframe por linhas
    # print(f"O tipo de dado é: {type(df_dict)}") # == lista

    json_str = df.to_json(orient='records') # ordena o dataframe por linhas
    print(type(json_str))
    stud_obj = json.loads(json_str) # Passa uma string JSON válida e converte para um dicionário Python
    print(type(stud_obj))
    json_obj = json.dumps(stud_obj) # Converte um objeto Python em uma str JSON
    print(type(json_obj))


    #? Não consigo ver como um arquivo JSON no navegador, mesmo após instalar a extensão
    # print(type(json.dumps(df_dict)))
    return json_obj

# Executa a API
# if __name__ == "__main__": # Modificação necessária para fazer o deploy (Não aceita a execução do codigo se for importado por um outro arquivo)

app.run(debug=True) #Não precisa ficar reiniciando o código