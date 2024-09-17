"""
Considere que o arquivo “ips.txt” apresenta uma listagem com os endereços IPs que acessaram um site.
Veja abaixo um exemplo de arquivo de texto nesse formato:
203.0.113.1
198.51.100.2
203.0.113.3
198.51.100.4
203.0.113.5
A partir desse arquivo, gere um novo arquivo com uma listagem de IPs únicos (sem valores repetidos).
"""


with open('ips.txt', 'r') as arquivo:
    set_ips = set()
    for linha in arquivo:
        set_ips.add(linha.replace("\n", ""))
    print(set_ips)

with open('ips_unicos.txt', 'w') as arquivo:
    lista_ips = list(set_ips)
    for i in range(len(lista_ips)):
        arquivo.write(f'{lista_ips[i]}\n')
