nome = ''

while len(nome) <= 3:
    nome = input('Informe seu nome \n')
    if len(nome) <= 3:
        print('Nome deve ter mais que 3 caracteres')

idade = -1
while idade < 0 or idade > 150:
    idade = int(input('Informe a idade \n'))
    


print(nome)