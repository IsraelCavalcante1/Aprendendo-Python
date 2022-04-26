#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = int(input('Qual o valor do produto?'))
novo = preco - (preco * 5 / 100)

print(f'O preço do produto sem desconto é: R${preco:.2f}')
print(f'O valor com os 5% de desconto ficará: R${novo:.2f}')