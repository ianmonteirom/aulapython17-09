"""
Considere o arquivo “foods.txt”, onde cada linha possui três campos:
NAME,ID,FAVORITEFOOD
Veja abaixo um exemplo de arquivo de texto nesse formato:
Michael Johnson,3,steak
Emily Davis,4,ice cream
William Brown,5,pasta
Sarah Miller,6,tacos
Daniel Taylor,7,burgers
Escreve um programa que leia esse arquivo e informe o alimento preferido pela maioria das pessoas.
"""

with open('foods.txt', 'r') as foods:
    vezes = []
    for linha in foods:
        palavras = linha.split(",")
        vezes.append(palavras[2].replace("\n", ""))
    print(vezes)