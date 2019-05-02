nota1 = float(input('informe a nota do primeiro semestre \n'))
nota2 = float(input('informe a nota do segundo semestre \n'))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
	print(f'aprovado com média: {media} \n')
elif media < 7:
	print(f'reprovado com média: {media} \n')
elif media == 10:
	print(f'Aprovado com Distinção: nota: {media} \n')
else:
	print('parametro errado')