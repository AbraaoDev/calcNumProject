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

# Retorna todo o dataframe no formato json
@app.route('/listar_all', methods=['GET'])
def listar_all():
    df = pd.read_csv('BrasileiraoSerieA.csv')

    # Tratamento de valores 
    df['POSICAO'].replace({"MEIO CAMPO": "MEIO-CAMPO"}, inplace=True)

    peso_medio = df['PESO'].mean()
    peso_medio = round(peso_medio, 2)
    df.update(df['PESO'].fillna(peso_medio))

    altura_media = df['ALTURA'].mean()
    altura_media = round(altura_media,2)
    df.update(df['ALTURA'].fillna(altura_media))

    idade_media = df['IDADE'].mean()
    idade_media = round(idade_media)
    df.update(df['IDADE'].fillna(idade_media))

    # Cria um database para cada posição e cria um arquivo .json com base no dataframe
    df_atacante = df.loc[df['POSICAO']=="ATACANTE"]
    json_str_atacante = df_atacante.to_json(orient="records")
    json_obj_atacante = json.loads(json_str_atacante)
    json_obj_atacante = json.dumps(json_obj_atacante)
    with open("../json/atacantes.json", "w") as outfile:
        outfile.write(json_obj_atacante)

    df_defensor = df.loc[df['POSICAO']=="DEFENSOR"]
    json_str_defensor = df_defensor.to_json(orient="records")
    json_obj_defensor = json.loads(json_str_defensor)
    json_obj_defensor = json.dumps(json_obj_defensor)
    with open("../json/defensores.json", "w") as outfile:
        outfile.write(json_obj_defensor)

    df_meiocampo = df.loc[df['POSICAO']=="MEIO-CAMPO"]
    json_str_meiocampo = df_meiocampo.to_json(orient="records")
    json_obj_meiocampo = json.loads(json_str_meiocampo)
    json_obj_meiocampo = json.dumps(json_obj_meiocampo)
    with open("../json/meiocampos.json", "w") as outfile:
        outfile.write(json_obj_meiocampo)

    df_goleiro = df.loc[df['POSICAO']=="GOLEIRO"]
    json_str_goleiro = df_goleiro.to_json(orient="records")
    json_obj_goleiro = json.loads(json_str_goleiro)
    json_obj_goleiro = json.dumps(json_obj_goleiro)
    with open("../json/goleiros.json", "w") as outfile:
        outfile.write(json_obj_meiocampo)

    json_str = df.to_json(orient='records') # ordena o dataframe por linhas
    json_obj = json.loads(json_str) # Passa uma string JSON válida e converte para um dicionário Python
    json_obj = json.dumps(json_obj) # Converte um objeto Python em uma str JSON
    with open("../json/jogadores.json", "w") as outfile:
        outfile.write(json_obj)

    return json_obj

# Executa a API
if __name__ == "__main__": # Modificação necessária para fazer o deploy (Não aceita a execução do codigo se for importado por um outro arquivo)
    app.run(debug=True) #Não precisa ficar reiniciando o código