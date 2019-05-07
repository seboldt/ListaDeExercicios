n1 = float(input('informe me dia do primeiro trimeste \n'))
n2 = float(input('informe a media do segundo trimestre \n'))
n3 = float(input('informe a nota do terceiro trimestre \n'))


media = (n1 + n2 +n3) / 3

print(f'A media do aluno foi: {media}')

if media == 10:
    print('Aprovado com Distinção')
elif media > 10:
    print('Infomado valores errados para calculo da nota')
elif media >=7:
    print('Aprovado')
else:
    print('Reprovado')
