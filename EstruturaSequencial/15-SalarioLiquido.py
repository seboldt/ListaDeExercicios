vHora = float(input('Informe valor hora: \n'))
horaMes = float(input('Informe total de horas trabalhadas por mes \n'))

salarioBruto = vHora * horaMes
print(f'Salario Bruto: {salarioBruto}')

ir = salarioBruto * 0.11
print(f'IR: {ir}')

inss = salarioBruto * 0.08
print(f'INSS: {inss}')

sindicato = salarioBruto * 0.05
print(f'Sindicato: {sindicato}')

salarioLiquido = salarioBruto - ir - inss - sindicato
print(f'Salario Liquido: {salarioLiquido}')


