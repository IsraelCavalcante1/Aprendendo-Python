'''Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''


relatorio = dict()
for c in range (0, 1):
    relatorio['nome'] = str(input('Nome do aluno? '))
    relatorio['media'] = float(input('Qual a média do aluno? '))
    relatorio['situacao'] = 'pendente'
    if relatorio['media'] >= 5 and relatorio['media'] < 7:
        relatorio['situacao'] = 'Recuperação'
    elif relatorio['media'] < 5:
        relatorio['situacao'] = 'Reprovado'
    elif relatorio['media'] > 7:
        relatorio['situacao'] = 'Aprovado'
print('-'* 26)
print(f'Nome é {relatorio["nome"]}')
print(f'Média é {relatorio["media"]}')
print(f'Situação é: {relatorio["situacao"]}')
print('-'* 26)