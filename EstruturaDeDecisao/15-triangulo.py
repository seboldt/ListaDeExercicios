l1 = float(input('Informe lado 1 \n'))
l2 = float(input('Informe lado 2 \n'))
l3 = float(input('Informe lado 3 \n'))


if l1 + l2 >= l3 and l1 + l3 >= l2 and l2 + l3 >= l1:
    print('É um triangulo')

    if l1 == l2 and l1 == l3:
        print('Triangulo Equilatero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('triangulo Isosceles')
    else:
        print('Triangulo Escaleno')

else:
    print('não é um triangulo')