from datetime import datetime

jogo = datetime.strptime("20/10/2016", '%d/%m/%Y')
print(datetime.today() - jogo)