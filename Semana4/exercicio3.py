from datetime import datetime

#nasc = input('Digite a data de nascimento (00/00/0000): ')
nasc = "24/10/2000"
nasc = datetime.strptime(nasc, '%d/%m/%Y')
hoje = datetime.today()

anos = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))

print(anos)