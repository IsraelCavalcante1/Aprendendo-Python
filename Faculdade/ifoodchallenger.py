INDEX_NOME = 0
INDEX_NOTA = 1
INDEX_DISTANCIA = 2

def ordenar_nota_decrescente(restaurantes):
    for i in range(len(restaurantes) - 1):
        for j in range(len(restaurantes) - 1):
            if restaurantes[j][INDEX_NOTA] < restaurantes[j + 1][INDEX_NOTA]:
                restaurantes[j], restaurantes[j + 1] = restaurantes[j + 1], restaurantes[j]


def desempatar_pela_distancia_crescente(restaurantes):
    for i in range(len(restaurantes) - 1):
        if restaurantes[i][INDEX_NOTA] == restaurantes[i + 1][INDEX_NOTA]:
            if restaurantes[i][INDEX_DISTANCIA] > restaurantes[i + 1][INDEX_DISTANCIA]:
                restaurantes[i], restaurantes[i + 1] = restaurantes[i + 1], restaurantes[i]


def ordenar_restaurantes(restaurantes):
    ordenar_nota_decrescente(restaurantes)
    desempatar_pela_distancia_crescente(restaurantes)

def exibir_tabela_ordenada():
    if len(restaurantes) > 0:
        print('')
        print("Seja bem-vindo ao menu de Restaurantes do iFood: ")
        print('')
        print(f"{'Restaurante': <15} {'Avaliação': <15} {'Distância': <15}")
    for r, n, d in restaurantes:
        print(f"{r: <15} {n: <15} {d: <15}")


            # LISTA COM RESTAURANTES
restaurantes = [["Habib's", 3.9, 3.8], # RESTAURANTE, NOTA, DISTÂNCIA
                ["Pizza Hut", 4.8, 3.2],
                ["Subway", 4.0, 3.7],
                ["McDonald's", 3.6, 7.8],
                ["Taco Bell", 4.1, 3.6],
                ["Sara Sushi", 4.8, 3.0]]

            # CHAMANDO FUNÇÕES
ordenar_restaurantes(restaurantes)
exibir_tabela_ordenada()
