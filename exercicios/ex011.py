#cada 2m² precisa de 1l pra ser pintado

largura = float(input('Qual a largura da parede?'))
altura = float(input('Qual a altura da parede?'))
area = largura * altura
soma = area / 2



print(f'Sua parede tem a dimensão de: {area}m²')
print(f'Para pintar essa parede você precisará de: {soma}l')
