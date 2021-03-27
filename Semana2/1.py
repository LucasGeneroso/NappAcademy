from massa_dados import lista_pessoas

def spend_by_login(login):
    for pessoa in lista_pessoas:
        username = pessoa[0]
        genero = pessoa[1]
        gasto = pessoa[2]

        if username == login:
            print(pessoa)   
    return

def sum_by_login(login):
    soma = 0
    for pessoa in lista_pessoas:
        if pessoa[0] == login:
            try:
                soma +=  float(pessoa[2]) 
            except ValueError:
                pass 
    return soma      

if __name__ == "__main__":
    login = 'daniellemosley'
    spend_by_login(login)
    print(f'A soma total é: {sum_by_login(login)}')
    