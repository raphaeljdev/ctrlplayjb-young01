saldo = 0
extrato = ""

while True:
    print("\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == 'd':
        valor = float(input("Valor a depositar: "))
        saldo += valor
        extrato += f"Depósito de R${valor:.2f}\n"
    elif opcao == 's':
        valor = float(input("Valor a sacar: "))
        if valor <= saldo:
            saldo -= valor
            extrato += f"Saque de R${valor:.2f}\n"
        else:
            print("Saldo insuficiente.")
    elif opcao == 'e':
        print("\n--- Extrato ---")
        print(extrato if extrato else "Nenhuma movimentação.")
        print(f"Saldo atual: R${saldo:.2f}")
    elif opcao == 'q':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
