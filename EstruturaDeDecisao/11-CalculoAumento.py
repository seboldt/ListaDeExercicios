salario = float(input('Valor do salario\n'))

if salario <= 280:
	aumento = 20
elif salario >280 and salario <=700:
	aumento = 15
elif salario > 700 and salario <= 1500:
	aumento = 10
elif salario > 1500:
	aumento = 5

valorAumento = (salario * (aumento/100))

print(f'Salario atual: {salario} \nPorcentagem de aumento: {aumento} \nValor do aumento: {valorAumento} \nNovo Slario: {salario+valorAumento}')

