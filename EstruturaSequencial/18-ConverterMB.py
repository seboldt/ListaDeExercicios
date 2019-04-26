import math

arquivo = float(input('informe o tamanho do arquivo em MB \n'))
velocidade = float(input('informe sua velocidade de internet \n'))

mbps = velocidade / 8

tempo = (arquivo / mbps) / 60

print(f'o arquivo vai levar {math.ceil(tempo)} minutos para terminar o download')