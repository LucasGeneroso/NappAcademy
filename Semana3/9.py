import csv
from usernames import Username

def carregar_arquivo(path):
    """
    Função que recebe a string com o arquivo, abre o arquivo CSV
    com o reader e carrega os dados em uma lista retornada.
    Args:
        path (String): Nome do arquivo
    Returns:
        (List): Lista com todos os registros
    """
    local_list = []
    with open(path, "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for line in csv_reader:
            local_list.append(
                Username(
                    name = line['name'],
                    username = line['username'],
                    credit_card = line['credit_card'],
                    credit_card_expire = line['credit_card_expire'],
                    birthdate = line['birthdate'],
                    gender = line['gender']
                )
            )
    return local_list

if __name__ == "__main__":
    path = 'usernames.csv'
    lista = []
    lista_substring = []
    lista_start = []
    lista = carregar_arquivo(path)
    for p in lista:
        if p.is_subtring_credit_card():
            lista_substring.append(p.__dict__)
        if p.is_start_subtring_credit_card():
            lista_start.append(p.__dict__)
    print(lista_substring)
    print(lista_start)