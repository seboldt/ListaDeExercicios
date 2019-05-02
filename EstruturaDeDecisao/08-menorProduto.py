n1 = float(input('informe valor do primeiro produto \n'))
n2 = float(input('informe valor do segundo produto \n'))
n3 = float(input('informe valor do terceiro produto \n'))

	
if n1 < n2 and n1 < n3:
	print(f'O produto mais barato é o primeiro {n1}')
elif n2 < n1 and n2 < n3:
	print(f'O produto mais barato é o segundo {n2}')
elif n3 < n1 and n3 < n2:
	print(f'O produto mais barato é o terceiro {n3}')