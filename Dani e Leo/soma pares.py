#Faca um programa que calcule e mostre a soma dos 50 primeiros numeros pares.
soma = 0
cont = 0
for c in range (1, 101):
    if c % 2 == 0:
        soma += c
        cont += 1
print(f'{soma}')

