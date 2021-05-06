from datetime import datetime

#nasc = input('Digite a data de nascimento (00/00/0000): ')
nasc = "24/10/2000"
nasc = datetime.strptime(nasc, '%d/%m/%Y')
print(datetime.today() - nasc)