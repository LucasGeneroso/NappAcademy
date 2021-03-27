import csv
import json

def converter_url_em_lista(url):
    url = url.replace("'","")
    url = url.replace("[","")
    url = url.replace("]","")
    url = url.replace(" ","")
    url = url.split(",")
    return url

def carregar_dicionario_websites(path):
    """
    Função que recebe o nome do arquivo .CSV
    e extrai um dicionário, com usernames como chave e tupla de URLs.
    Args:
        path (String): Nome do arquivo
    Returns:
        Dicionário: Dicionário, cuja chave é o username
        e o valor são tuplas com URLs de websites.
    """
    local_list = {}
    with open(path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for line in reader:
            if line[0] == 'name':
                continue
            local_list[line[0]]=converter_url_em_lista(line[4])
    return local_list


if __name__ == "__main__":
    path = 'names.csv'
    dicionario = {}
    dicionario = carregar_dicionario_websites(path)
    json_object = json.dumps(dicionario, indent=4)
    print(json_object)