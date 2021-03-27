lista_nomes = ['Ana', 'Maria', 'José', 'Pedro', 'Elena', 'Helena', 'Elen']
vogais = ['A', 'E', 'I', 'O', 'U']

for nome in lista_nomes:
    if nome[0].upper() in vogais:
        print(nome)