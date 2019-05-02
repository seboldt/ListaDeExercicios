vHora = float(input('Informe valor hora: \n'))
horaMes = float(input('Informe total de horas trabalhadas por mes \n'))

salarioBruto = vHora * horaMes
print(f'Salario Bruto: {salarioBruto}')

if salarioBruto <= 900:
	vlIr = 0
elif salarioBruto <= 1500:
	vlIr = 0.05
elif salarioBruto <= 2500:
	vlIr = 0.1
elif salarioBruto > 2500:
	vlIr = 0.2



ir = salarioBruto * vlIr
print(f'IR: {ir}')

inss = salarioBruto * 0.11
print(f'INSS: {inss}')

sindicato = salarioBruto * 0.03
print(f'Sindicato: {sindicato}')

salarioLiquido = salarioBruto - ir - inss - sindicato
print(f'Salario Liquido: {salarioLiquido}')


