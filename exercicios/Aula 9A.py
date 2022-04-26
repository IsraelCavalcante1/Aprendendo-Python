#Manipulando texto


frase = 'Curso em Vídeo Python'
frase02 = '   Aprenda Python  '
dividido = frase.split()
print(f'{frase[:21]}') #O que será exibido da cadeia de letras/fatiamento
print(f'{frase[3]}') #Outro exemplo de fatiamento
print(f'{frase[0:15]}') #Outro tipo de fatiamento
print(f'{frase[0::2]}') # Não especifico qual o final da string, logo, irá até o final pulando de dois em dois
print(f'{frase[0::]}') # Aqui fará a mesma coisa da linha anterior, porém sem pular duas em duas letras
print(f'{frase[0:15:2]}') #Fatiamento pulando de duas em duas letras
print(len(frase)) #comprimento da frase
print(frase.count('o',0,13)) #Contar quantas letras especificadas com '' tem na cadeia de letras e depois até aonde quero que mostre
print(frase.find('deo')) #Localizar onde está a letra ou sequência da cadeia de letras, especificadas após o começo das aspas simples
print(frase.find('Android')) #Quando a string não existe, o valor retornado sempre será -1, pois ela não existe.
print('Curso' in frase) #Aqui ele retornará um valor sendo booleano True ou False, caso a palavra exista na cadeia de letras
print(frase.replace('Python', 'Android')) #Esse método é para alterar uma string, por exemplo aqui trocamos Python para Android e ele retornará o novo valor string
print(frase.upper()) #Essa linha de código é para colocar a string em maiúscula
print(frase.lower()) #Essa linha é ao contrário, serve para deixar a string totalmente minúscula
print(frase.capitalize()) #Essa é para colocar o começo da String em maiúsculo
print(frase.title()) #Ele colocará todo começo de String em letras maiúsculas
print(frase02.strip()) #Tirará todos os espaços inúteis do começo e do final
print(frase02.rstrip()) #Tirará todos os espaços inúteis do lado direito (right/final)
print(frase02.lstrip()) #Tirará todos os espaços inúteis do lado esquerdo (left/começo)
print(frase.split()) #Separa as strings após o espaçamento, também começa uma nova recontagem a cada string dividida, gera uma nova cadeia de caracteres
print('-'.join(frase))
print(frase.upper().count('O')) #Aqui fará a junção de duas funcionalidades para que a "count" funcione de forma adequada
print(len(frase)) #Outro exemplo de junção de duas funcionalidades, onde excluirá todos os espaçamentos inúteis para que a função "len" funcione adequadamente
print(dividido[3]) #Aqui eu peço para que mostre a variável da string que está com split (sendo dividida) e falo qual cadeia quero que seja mostrada
print(dividido[3][1]) #Aqui uso uma função para identificar a letra 1 na cadeia de letras 3







#As cadeias de letras sempre começam no número 0 e sempre que for especificar um número ele será um maior, pois ignorará o maior.




