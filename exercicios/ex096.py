'''Faça um programa que tenha uma função chamada área(),
que receba as dimensões de umterreno retangular (largura e comprimento) e mostre a área do terreno.'''

# def area(a, b):
#     a = a*b
#     print(a)
#
# # Programa Principal

# area(a=(float(input('Digite a largura (M): '))), b=float(input('Digite o comprimento (M): ')))


   # '''SOLUÇÃO ALTERNATIVA'''


def area (larg, comp):
    a = larg * comp
    print(f'Sua largura é {larg}m² e seu comprimento é {comp}m², por sua vez a área é de {a}m²')

largura = float(input('Qual a sua largura? (M): '))
comprimento = float(input('Qual o seu comprimento (M): '))
area(largura, comprimento)


