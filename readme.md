# Bola Na Rede
## Coleta de Dados e Harmonização
Projeto desenvolvido durante a disciplina de **Cálculo Numérico** (2021.2).

A equipe 3 foi designada a coletar os dados de todos os times que participaram do **Brasileirão Série A** no período 2020-21. 

Com os dados coletados, o objetivo deste projeto é montar o time perfeito e escolher o goleiro ideal utilizando métodos numéricos aprendidos durante a disciplina.

### Requisitos
Disponível no arquivo `requirements.txt`.

### Funcionamento
Os arquivos necessários são gerados por meio da API feita em Flask, esta lê uma base de dados em `.csv` e retorna um arquivo `.json` refente às quatro posições de campo(atacante, defensor, meio-campo e goleiro).

Sendo assim, basta executar o arquivo `main.py`. Neste arquivo contém todas as funções necessárias para calcular o Índice de Massa Corpórea de cada jogador e a Taxa Metabólica Basal. 

Demais informações quanto ao projeto podem ser acompanhadas na pasta **`documentos`**.

> **Equipe 3**: [Abraão](https://github.com/AbraaoDev), [Altamir](Altamirfl), Anderson, Eduardo Nunes, Élen, [Felipe Miranda](https://github.com/Mirandacc97), [Gabriel Mendes](https://github.com/Jesarus), Matheus Henrique e [Samantha](https://github.com/sammid37).

### Anotação 04/05/22 18:09
O arquivo main2.py foi criado como modo alternativo de estruturação da função main.py principal