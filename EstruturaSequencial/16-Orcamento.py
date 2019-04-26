import  math

m = float(input('informe o tamanho da area a ser pintada em metros quadrados \n'))

totalLatas = m / 54
valor = math.ceil(totalLatas) * 80

print(f'Comprar: {math.ceil(totalLatas)} de tinas \n Valor total R${valor}')

