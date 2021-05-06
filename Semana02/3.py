from massa_dados import lista_pessoas

def spend_by_subname(name):
    for pessoa in lista_pessoas:
        if str(name) in str(pessoa[0]):
            print(pessoa)        
    return

def sum_by_subname(name):
    soma = 0
    for pessoa in lista_pessoas:
        if name in pessoa[0]:
            try:
                soma +=  float(pessoa[2]) 
            except ValueError:
                pass 

    return float(round(soma,2)) 

if __name__ == "__main__":
    name = 'rews'
    spend_by_subname(name)
    print(f'A soma total é: {sum_by_subname(name)}')