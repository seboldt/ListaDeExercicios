sexo = input('informe o sexo M ou F \n')

h = float(input('informe a altura e metros \n'))

if sexo == 'M' or sexo == 'm':
	print(f'Masculino peso ideal: {(72.7*h)-58}')

elif sexo == 'F' or sexo == 'f':
	print(f'Feminino peso ideal: {(62.1*h)-44.7}')
else:
	print('Deve informar M ou F')
