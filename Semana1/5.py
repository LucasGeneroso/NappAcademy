lista_frases = ['Eu gosto de batatas', 'Eu estava andando de moto']
lista_frases += ['Ele estava comendo no restaurante']
lista_frases += ['O cachorro está passeando pelo parque']

new = []

for i in lista_frases:
    new.append(i.split(' '))

for i in new:
    for item in i:
        if 'ando' in item:
            print(item)
        if 'endo' in item:
            print(item)
        if 'indo' in item:
            print(item)

    



    
