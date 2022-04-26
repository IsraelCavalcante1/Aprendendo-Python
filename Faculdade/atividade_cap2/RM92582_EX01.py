from time import sleep

print('~' * 12, 'Calculadora de IMC', '~' * 12)
peso = float(input('Qual o seu peso em (KG): '))  # input de peso
altura = float(input('Diga sua altura (ex: 1.65): '))  # input de altura
imc = peso / altura ** 2  # cálculo para saber o imc

    # Condição para saber em qual categoria o usuário se encaixa
if imc <= 16.00:
    print(f'Seu IMC é {imc:.2f} e você está na categoria: Baixo peso Grau III')
elif imc >= 16.00 and imc <= 16.99:
    print(f'Seu IMC é {imc:.2f} e você está na categoria: Baixo peso Grau II ')
elif imc >= 17.00 and imc <= 18.49:
    print(f'Seu IMC é {imc:.2f} e você está na categoria: Baixo peso Grau I ')
elif imc >= 18.50 and imc <= 24.99:
    print(f'Seu IMC é {imc:.2f} e você está na categoria: Peso ideal ')
elif imc >= 25.00 and imc <= 29.99:
    print(f'Seu IMC é {imc:.2f} e você está na categoria: Sobrepeso ')
elif imc >= 30.00 and imc <= 34.99:
    print(f'Seu IMC é {imc:.2f} e você está na categoria: Obesidade grau I ')
elif imc >= 35.00 and imc <= 39.99:
    print(f'Seu IMC é {imc:.2f} e você está na categoria: Obesidade grau II ')
else:
    print(f'Seu IMC é {imc:.2f} e você está na categoria: Obesidade grau III ')
sleep(0.5)
print('*'*13, 'Finalizando...', '*'*13)
sleep(500)
