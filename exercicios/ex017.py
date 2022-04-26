# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.



'''oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comrpimento do cateto adjacente: '))
hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hipotenusa:.2f} ')'''

#acima vimos a forma sem importação com cálculos manuais


import math

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente'))
hipotenusa = math.hypot(oposto, adjacente)
print(f'A hipotenusa irá medir: {hipotenusa:.2f}')

#Acima vemos com importação da biblioteca math

