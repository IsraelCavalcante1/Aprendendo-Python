# Programa que imprime a quantidade de números ímpares de x até n.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

for c in range (n1, n2+1, 1):
    if c % 2 != 0 :
        print(c)



