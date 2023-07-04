menu = """

[d] Depositar
[s] sacar
[e] Extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
     valor = float(input("Informe o valor do depósito: "))

     if valor > 0:
         saldo += valor
         extrato+= f"Deposito de R$ {valor:.2f} \n"
         print("Deposito com sucesso!!")
     else:
         print("Operação falhou! O valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente para realizar a operação!")

        elif excedeu_limite:
            print(f"Valor ultrapassa o limite permitido. Limite disponível")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
         saldo -= valor
         extrato += f"Saque de R$ {valor:.2f}\n"
         numero_saques += 1
         print("Saque efetuado com sucesso!!")
        else:
            print("Operação falhou! o valor informado é invalido.")

    elif opcao == "e":
       print("\n================ EXTRATO ================")
       print("Não foram realizadas movimentações."if not extrato else extrato)
       print(f"\nSaldo: R$ {saldo:.2f}")
       print("==========================================")

    elif opcao == "q":
       break
else:
    print("Operação inválida, por favor selecione novamente a operaçõ desejada")
