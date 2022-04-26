'''Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A"
> Em que posição ela aparece a primeira vez
> Em que posição ela aparece a última vez
'''

frase = str(input('Qual a frase a ser analisada?')).strip().upper()
# quantidade = frase.upper().count('A')
# primeira = frase.upper().find('A')
# final = frase.upper().rfind('A')



print(f'Sua frase contem: {frase.upper().count("A")} letras A')
print(f'A primeira posição que sua letra aparece é: {frase.upper().find("A")+1} ')
print(f'A última posição em que sua letra aparece é: {frase.upper().rfind("A")+1}')