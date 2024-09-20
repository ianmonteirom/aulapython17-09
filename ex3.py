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
    comidas = []
    qntd = {}
    for i in range(len(vezes)):
        if vezes[i] not in comidas:
            comidas.append(vezes[i])
            qntd[vezes[i]] = 1
        if vezes[i] in comidas:
            qntd[vezes[i]] += 1

maior_valor = 0
maior_produto = 0

for chave, valor in qntd.items():
    if valor > maior_valor:
        maior_valor = valor
        maior_produto = chave


print(f'A comida preferida pela maioria é {maior_produto} com {maior_valor - 1} preferências.')
