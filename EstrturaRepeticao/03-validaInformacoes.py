nome = ''

while len(nome) <= 3:
    nome = input('Informe seu nome \n')
    if len(nome) <= 3:
        print('Nome deve ter mais que 3 caracteres')

idade = -1
while idade < 0 or idade > 150:
    idade = int(input('Informe a idade \n'))
    if idade < 0 or idade > 150:
        print('idade invalida')

salario = -2

while salario < 0:
    salario = float(input('informe seu salario \n'))
    if salario < 0:
        print('salario informado é invalido')


sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = input('Informe o sexo \nM-Masculino \nF-Feminino\n').upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo invalido')

estado_civil = 'A'
tipo = 'SCVD'

while tipo.find(estado_civil) < 0:
    estado_civil = input('informe estado civil \nS-Solteiro \nC-Casado \nV-Viuvo \nD-Divorciado\n').upper()
    if tipo.find(estado_civil) < 0:
        print('estado civil invalido')


print(nome)
print(salario)
print(sexo)
print(estado_civil)