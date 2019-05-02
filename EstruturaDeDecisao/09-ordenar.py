n1 = (input('informe valor do primeiro produto \n'))
n2 = (input('informe valor do segundo produto \n'))
n3 = (input('informe valor do terceiro produto \n'))

if n1 > n2 and n1 > n3:
	primeiro = n1
	if n2 > n3:
		segundo = n2
		terceiro = n3
	else:
		segundo = n3
		terceiro = n2
elif n2 > n1 and n2 > n3:
	primeiro = n2
	if n1 > n3:
		segundo = n1
		terceiro = n3
	else:
		segundo = n3
		terceiro = n1
elif n3 > n1 and n3 > n2:
	primeiro = n3
	if n2 > n1:
		segundo = n2
		terceiro = n1
	else:
		segundo= n1
		terceiro = n2

print(f'Primeiro: {primeiro} \nSegundo: {segundo} \nTerceiro: {terceiro} \n')