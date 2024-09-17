"""
Considere que o arquivo “notas.txt” apresenta uma listagem com os dados dos alunos de uma turma. Cada linha
do arquivo apresenta os dados de um aluno, no formato:
RM,NOME,NOTA1,NOTA2,NOTA3,NOTA4
Veja abaixo um exemplo de arquivo de texto nesse formato:
2101254,Benicio Pires,3.6,10.0,8.5,7.8
2101624,Bruna Goncalves,9.5,8.0,6.0,5.5
2101533,Danilo Jesus,7.8,8.7,6.5,9.0
2101969,Ana Carolina Silva,8.1,7.3,9.2,8.8
2101779,Lavinia Duarte,9.0,8.0,8.5,9

Implemente um programa que leia o arquivo indicado e, a partir desse arquivo, gere dois novos arquivos:
• Arquivo “aprovados.txt” contendo uma listagem dos alunos aprovados na disciplina, contendo
RM,NOME,MEDIA do aluno
• Arquivo “reprovados.txt” contendo uma listagem dos nomes dos alunos reprovados na disciplina,
contendo RM,NOME,MEDIA do aluno.
Para o aluno ser aprovado ele deve ter média igual ou superior a 6.0.
"""

with open('aprovados.txt', 'w') as arquivo:
    arquivo.write('')

with open('reprovados.txt', 'w') as arquivo:
    arquivo.write('')

with open('notas.txt', 'r') as arquivo:
    notas = []
    for linha in arquivo:
        palavras = linha.replace("\n", "").split(",")
        notas = palavras[-4:]
        soma_notas = []
        for i in range(len(notas)):
            soma_notas.append(float(notas[i]))
        media = (sum(soma_notas)) / 4
        print(palavras)
        if media >= 6:
            with open('aprovados.txt', 'a') as aprovados:
                aprovados.write(f'{palavras[0]},{palavras[1]},{str(media)}\n')
        elif media <= 6:
            with open('reprovados.txt', 'a') as reprovados:
                reprovados.write(f'{palavras[0]},{palavras[1]},{str(media)}\n')
