galera = list()
pessoa = dict()
cont = 0
soma = 0

while True:
    cont = cont + 1
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa ['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas Masculino ou Feminino.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        print(f'Erro! Responda apenas Sim ou Não!')
    if resp == 'N':
        break
media = soma / cont
print('-=' * 30 )
print(f'Ao todo temos {cont} pessoas cadastradas')
print(f'A média de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}.', end=' ')
print()
print('Lista das pssoas que estão acima da média de idade: ', end='')
for p in galera:
    if p['idade'] > media:
        print(f'{p["nome"]} com {p["idade"]} anos. ', end='')
print()
print(f'-=' * 15, 'FINAL', '-=' * 15)

