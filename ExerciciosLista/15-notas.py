valores = []
valor = 0

print('Informe -1 para Parar')
while valor != -1:
    valor = float(input('Informe o valor \n'))
    if valor != -1:
        valores.append(valor)

print(f'A-Fotal de valores: {len(valores)}')
print(f'B-Todos os valores: {valores}')
valores.reverse()
print(f'C-Todos os valores ao contrario: {valores}')


soma = 0

for nota in valores:
    soma += nota

print(f'D-Soma dos valores: {soma}')

media = soma / len(valores)

print(f'E-Media dos valores: {media}')

acima = 0
abaixo = 0

for nota in valores:
    if nota >= 7:
        acima+= 1
    elif nota < 7:
        abaixo+= 1

print(f'F-Valores acima de 7: {acima}')
print(f'G-Valores abaixo de 7: {abaixo}')
print('Encerrando Programa')




