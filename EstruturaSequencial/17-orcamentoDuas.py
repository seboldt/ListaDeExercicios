import  math

m = float(input('informe o tamanho da area a ser pintada em metros quadrados \n'))

litros = (m / 6) * 1.1

lata = litros / 18
galao = litros / 3.5
 
valorLata = math.ceil(lata) * 80
valorGalao = math.ceil(galao) * 25

mistaLatas = int(litros / 18)
mistaGaloes = (litros - (mistaLatas * 18)) / 3.6

valorMista = (mistaLatas * 80) + (math.ceil(mistaGaloes) *25)

print(f'Comprar: {math.ceil(lata)} latas de tinas \n Valor total R${valorLata}')
print(f'Comprar: {math.ceil(galao)} galoes de tinas \n Valor total R${valorGalao}')
print(f'Comprar: {mistaLatas} latas de tintas e {math.ceil(mistaGaloes)} galoes \n Valor total: R$ {valorMista}')
