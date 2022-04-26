#Escreva um programa que leia 10 numeros e escreva o menor valor lido e o maior valor lido.
maior = 0
menor = 99999999999999999999
for n in range (0, 3):
    numero = int(input('Digite um valor: '))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero



print(maior, menor)

