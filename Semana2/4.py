from massa_dados import lista_pessoas

def spend_by_login(login, limit=1000):
    for pessoa in lista_pessoas:
        try:
            if login in pessoa[0]  and (float(pessoa[2]) <= limit):
                print(pessoa) 
        except ValueError:
            pass 
    return  

def sum_by_login(login, limit=1000):
    soma = 0
    for pessoa in lista_pessoas:
        try:
            if login in pessoa[0] and (float(pessoa[2]) <= limit):
                soma += float(pessoa[2]) 
        except ValueError:
            pass 

    return float(round(soma,2)) 

if __name__ == "__main__":
    login = 'hannah'
    spend_by_login(login, 600)
    print(f'A soma total até 600: {sum_by_login(login)}')
    print(f'A soma total até 1200: {sum_by_login(login, 1200)}')
