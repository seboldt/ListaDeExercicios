t = int(input('Informe o tipo de carne \n1-File Duplo \n2-Alcatra \n3-Picanha\n'))

qtdade = float(input('Informe a quantidade de carne comprada \n'))

if t == 1:
    tipo = 'File Duplo'
    if qtdade <= 5:
        preco =  4.9
    else:
        preco = 5.8

elif t == 2:
    tipo = 'Alcatra'
    if qtdade <= 5:
        preco = 5.9
    else:
        preco = 6.8

elif t == 3:
    tipo = 'Picanha'
    if qtdade <= 5:
         preco= 6.9
    else:
        preco = 7.8

else:
    print('valor invalido \n')

total = qtdade * preco

pg = int(input('Informe a forma de pagament\n1-Dinheiro \n2-Cartao Tabajara \n'))

if pg == 1:
    forma = 'Dinheiro'

elif pg == 2:
    forma = 'Cartao Tabajara'
    total = total - (total * 0.05)


print(f'Quantidade: {qtdade} \nTipo de Carne: {tipo} \nPreço: {preco} \nForma de Pagamento: {forma} \nValor Total: {total} ')