user = 'admin'
senha = 'admin'

while user == senha:
    user = input('informe o usuario \n')
    senha = input('informe a senha \n')

    if user == senha:
        print('usuario e senha nao podem ser iguais')