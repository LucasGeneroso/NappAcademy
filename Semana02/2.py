from massa_dados import lista_pessoas

def spend_by_gender(gender):
    for pessoa in lista_pessoas:
        if pessoa[1] == gender:
            print(pessoa)   
    return

def sum_by_gender(gender):
    soma = 0
    for pessoa in lista_pessoas:
        if pessoa[1] == gender:
            try:
                soma +=  float(pessoa[2]) 
            except ValueError:
                pass 

    return float(round(soma,2)) 

if __name__ == "__main__":
    gender = 'M'
    spend_by_gender(gender)
    print(f'A soma total é: {sum_by_gender(gender)}')