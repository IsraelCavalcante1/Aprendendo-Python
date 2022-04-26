# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
# mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida

peso = float(input('Qual o seu peso em (KG): '))
altura = float(input('Diga sua altura (ex: 1.65): '))
soma = peso / altura**2

print(f'Seu IMC é: {soma}')

if soma < 18.5:
    print(f'Você precisa se alimentar melhor! Seu IMC está abaixo do peso ideal para sua altura x peso.')
elif soma < 25:
    print(f'Parabéns, seu peso está ideal para sua altura x peso, continue se alimentando bem! ')
elif soma < 30:
    print(f'Você está com um leve sobrepeso, se alimente melhor e pratique atividades físicas! ')
elif soma < 40:
    print(f'Você está obeso, pratique atividades físicas e se alimente melhor. ')
else:
    print(f'Você está em uma obesidade mórbida, precisa urgentemente fazer atividades físicas e dieta! ')
