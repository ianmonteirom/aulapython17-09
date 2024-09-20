"""
Considere um arquivo de texto com informações coletadas de 10 pilotos que dirigem carros elétricos. O arquivo
inclui os seguintes dados:
• Nome do piloto.
• Número do carro do piloto.
• Tempo de volta do piloto em segundos.
• Velocidade média do piloto em km/h durante a corrida.
• Consumo médio de energia em kilowatt-hora durante a corrida.
• Temperatura média do motor em graus Celsius durante a corrida.
• Posição final do piloto na corrida.
Veja abaixo um exemplo de arquivo de texto nesse formato:
John Doe,7,78.5,150.3,12.4,75,1
Jane Smith,14,79.2,149.8,12.6,76,2
Mike Johnson,22,80.1,148.7,12.8,74,3
Emily Davis,8,79.8,149.1,12.5,75,4
Com base no arquivo fornecido, desenvolva um programa que forneça as seguintes informações:
1. Consumo Médio de Energia: Calcule o consumo médio de energia (kWh) dos carros durante a corrida.
2. Piloto com o Menor Consumo de Energia: Identifique o nome do piloto cujo carro teve o menor consumo
de energia durante a corrida.
3. Piloto com o Maior Tempo de Volta: Determine o nome do piloto que completou a volta em maior tempo.
"""

pilotos = {}

with open('pilotos.txt', 'r') as arquivo_pilotos:
    for linha in arquivo_pilotos:
        dados = linha.replace("\n", "").split(",")
        for i in range(len(dados)):
            valores = []
            if i == 0:
                pilotos[dados[0]] = []
            else:
                for j in range(len(dados)):
                    if j != 0:
                        valores.append(float(dados[j]))
                pilotos[dados[0]] = valores

soma_consumo, maior_volta = 0, 0
menor_consumo = 9999999999
piloto_menor_consumo, piloto_maior_volta = '', ''

for chave, valor in pilotos.items():
    soma_consumo += valor[4]

    if valor[4] < menor_consumo:
        menor_consumo = valor[4]
        piloto_menor_consumo = chave

    if valor[2] > maior_volta:
        maior_volta = valor[2]
        piloto_maior_volta = chave

consumo_medio = soma_consumo / len(pilotos)

print(f'Consumo médio dos pilotos: {consumo_medio} kWh\n'
      f'Piloto com menor consumo de energia: {piloto_menor_consumo} com {menor_consumo} kWh\n'
      f'Piloto com maior tempo de volta: {piloto_maior_volta} com {maior_volta} segundos.')
