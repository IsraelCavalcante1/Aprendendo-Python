
inicio = int(input('Quantos termos?'))
termo1 = 0
termo2 = 1
print(f'{termo1} > {termo2}', end='')
contador = 3
while contador <= inicio:
    termo3 = termo1 + termo2
    print(f'> {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
