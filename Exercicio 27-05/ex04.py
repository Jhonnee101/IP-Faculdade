
#nome = str(input("Digite seu nome "))
#ano = int(input("Em que ano vc nasceu? "))
#idade = 2023- ano
#print (idade)

from datetime import datetime
nome = str(input("Digite seu nome "))
ano = int(input("Em que ano vc nasceu? "))
data = datetime(ano)
atual = datetime.now()
idade = data - atual
print (idade)