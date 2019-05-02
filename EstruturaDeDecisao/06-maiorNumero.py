n1 = float(input('informe primeiro numero \n'))
n2 = float(input('informe segundo numero \n'))
n3 = float(input('informe terceiro numero \n'))

	
if n1 > n2 and n1 >n3:
	print(f'O maior é {n1}')
elif n2 > n1 and n2 > n3:
	print(f'O maior é {n2}')
elif n3 > n1 and n3 > n2:
	print(f'O maior é {n3}')