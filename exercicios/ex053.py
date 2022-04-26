# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #separa a frase em coleções
junto = ''.join(palavras) #juntar tudo
inverso = '' #variável vazia
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra] #INVERTENDO A STRING (FRASE)
print(junto, inverso)
if inverso == junto: #TESTANDO SE A FRASE É UM PALÍNDROMO
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')