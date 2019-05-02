turno = input('Informe turno de estudo \nM-Matutino\nV-Vespertino\nN-Noturno\n')

if turno == 'M' or turno == 'm':
	print('Bom dia!')
elif turno == 'V' or turno == 'v':
	print('Boa tarde!')
elif turno == 'N' or turno == 'n':
	print('Boa noite!')
else:
	print('Valor Inválido!')