peso = float(input('Informe o peso total de peixe pescado \n'))


if peso <= 50:
	print(f'Nao teve excesso')

else:
	excesso = peso - 50
	multa = excesso * 4
	print(multa)
