from time import sleep

print(f'~' * 13, 'O algoritmo da sorte de Fibonnaci.', '~' * 13)
while True:
    num = int(input("Digite um número para descobrir se ele está na sequência Fibonacci: "))
    n1 = 0
    n2 = 1
    n3 = 1
    if num == 0 or num == 1:
        print(f"Ação bem sucedida, o número {num} está na sequência de Fibonacci!")
    else:
        while n1 < num:
            n1 = n2 + n3
            n3 = n2
            n2 = n1
        if n1 == num:
            print(f"Ação bem sucedida, o número {num} está na sequência de Fibonacci!")
        else:
            print(f"Ação falhou, o número {num} não está na sequência de Fibonacci!")
    print('_' * 53)
    resp = str(input('Você quer checar algum outro número? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Finalizando...')
sleep(0.5)
