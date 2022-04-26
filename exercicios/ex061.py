print('Gerador de PA')
print('-=' * 7)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}' ,end='')
    print(f' > ' if cont < 10 else '',end='')
    termo = termo + razão
    cont = cont + 1

