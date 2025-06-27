print("Escolha uma Ação")
print("1. Depositar")
print("2. Sacar")
print("3. Extrato")
print("4. Sair")


saldo = 2500
extrato = saldo


while True:
    acao = input("Digite sua opção")


    if acao == '1':
        print("Digite o Valor para ser Depositado")
        depositar = int(input("-"))
        if depositar <= 0:
            print("Valor inválido")
        else:
            saldo += depositar
            print("Seu deposito foi efetuado")
    elif acao == '2':
        print ("Digite o Valor para ser Sacado")
        sacar = int(input("-"))
        if sacar <= 0:
            print("Valor inválido")
        elif sacar > saldo:
            print("Saldo Insuficiente")
        else:
            saldo -= sacar
            print("Seu saque foi efetuado")
    elif acao == '3':
        print("Seu saldo é:", saldo)
    elif acao == '4':
        print("Saindo do Sistema")
        break
