# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima PODEM FORMAR um Triângulo! ')
    if r1 == r2 == r3:
        print('A forma do Triângulo é EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('A forma do Triângulo é ESCALENO')
    else:
        print('A forma do Triângulo é ISÓSCELES')




else:
    print('As retas acima não podem formar um Triângulo!')