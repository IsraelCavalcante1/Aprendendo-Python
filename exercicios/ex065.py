# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = '0'
soma = 0
cont = 0
maior = 0
menor = 0



while continuar not in ('Nn'):
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    continuar = str(input('Você quer continuar? [S/N]: ')).upper().strip()[0]
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

média = soma / cont
print(f'A soma entre os valores digitados é: {soma} e a média é {média:.2f}. O maior número foi {maior} e o menor número foi {menor} ')



