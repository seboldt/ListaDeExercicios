n1 = float(input('Informe a nota do primeiro bimestre \n'))
n2 = float(input('Informe a nota do segundo bimestre\n'))

media = (n1 + n2) / 2

if media >= 9:
	conceito = 'A'
elif media >= 7.5 and media < 9: 
	conceito = 'B'
elif media >= 6 and media < 7.5:
	conceito = 'C'
elif media >= 4 and media < 6:
	conceito = 'D'
elif media < 4:
	conceito = 'E'


if conceito == 'A' or conceito == 'B' or conceito == 'C':
	resultado = 'Aprovado'

elif conceito == 'D' or conceito == 'E':
	resultado = 'Reprovado'


print(f'Nota 01: {n1} \nNota 02: {n2} \nMedia: {media} \nConceito: {conceito} \nResultado: {resultado}')