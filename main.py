valorTotal = 0
def volumeFeijoada():
    while True:
        volume = float(input('Entre com a quantidade em ml desejada:'))
        if 300 <= volume <= 5000:
            return volume * 0.08
        else:
            print('Não aceitamos porções menores que 300ml ou maiores que 5L')
            continue
def opcaoFeijoada ():
    print('B - Básica (Feijão + paio + costelinha )')
    print('P - Premium (Feijão + paio +costelinha + partes de porco')
    print('S - Suprema (Feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon')
    while True:
        opcao = input('Entre com a opção desejada:')
        if opcao == 'B' or opcao == 'b':
            return volume * 1.00
        elif opcao == 'P' or opcao == 'p':
            return volume * 1.25
        elif opcao == 'S' or opcao == 's':
            return volume * 1.50
        else:
            print('Opção inválida!')
            continue
def acompanhamentoFeijoada():
    print('0 - Nao desejo acompanhamentos')
    print('1 - 200g de arroz')
    print('2 - 150G de farofa especial')
    print('3 - 100g de couve cozida')
    print('4 - 1 laranja descascada')
    acumulador= 0
    while True:
        acompanhamento = float(input('Entre com o acompanhamento desejado:'))
        if acompanhamento == 1:
            acumulador = acumulador + 5
        elif acompanhamento == 2:
            acumulador = acumulador + 6
        elif acompanhamento == 3:
            acumulador = acumulador + 7
        elif acompanhamento == 4:
            acumulador = acumulador + 3
        elif acompanhamento == 0:
            break
    return acumulador

print('Bem vindo a Feijoada do Eduardo da Costa Santos ★')
volume = volumeFeijoada()
opcao = opcaoFeijoada()
acompanhamento = acompanhamentoFeijoada()
valorTotal = volume + opcao + acompanhamento
print('O valor a ser pago é R${:.2f}'.format(valorTotal))
