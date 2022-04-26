
import json #Formato padrão da API
import requests
import mysql.connector

 #Caso não haja API, MirageJS para uma fake api
response = requests.get("https://apibolanarede3.herokuapp.com/listar_all") # <- Alimentação
#req
print(response.status_code) 
#return API
print(response.content) 
 #serializa
dados = json.loads(response.content)

for listar_all in dados: #passa pelo JSON
    print(listar_all)  #inserir variável de cada jogador 



#coleta, atribuindo o "tipo" de forma separada
dbPlayer = {}

dbPlayer["name"] = dados["name"]
dbPlayer["id"] = dados["id"]
dbPlayer["height"] = dados["height"]
dbPlayer["weight"] = dados["weight"]

type_Player = []

for tipo in dados["types"]:
    type_Player.append(tipo["type"]["name"])

dbPlayer["type"] = type_Player

#coleta + armazenamento para o BANCO

name_Players = ["", ""] #filtro de pesquisa

player_list = []

for name in name_Players:
    data = requests.get(""+ name) #api or fake api
    data_json = json.loads(data.content)
    
    jogador = {}

    jogador["name"] = data_json["name"]
    jogador["id"] = data_json["id"]
    jogador["height"] = data_json["height"]
    jogador["weight"] = data_json["weight"]  

    type_Player = []

    for tipo in data_json["types"]:
        type_Player.append(tipo["type"]["name"])

    jogador["type"] = type_Player
    
    player_list.append(jogador) 



#Conexão com o banco de dados
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='equipe3', 
    database='randomDB'
)



mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)

for jogador in player_list:
    type_Player = jogador["type"][0]
    
    query = "INSERT INTO tb_player VALUES(%s, '%s', %s, %s, (SELECT id FROM tb_type WHERE type LIKE '%s')) " % (jogador["id"], jogador["name"], jogador["height"], jogador["weight"], type_Player)
    
    mycursor.execute(query)

    #Fazer a confirmação da inserção    
    mydb.commit()

    print(mycursor.rowcount, " registro inserido.")

# Forçando o fechamento da tabela
mydb.close()