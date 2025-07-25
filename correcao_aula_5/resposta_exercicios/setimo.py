while True:
    print("\n[1] Somar\n[2] Subtrair\n[3] Multiplicar\n[4] Dividir\n[0] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        break

    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))

    if opcao == '1':
        print("Resultado:", n1 + n2)
    elif opcao == '2':
        print("Resultado:", n1 - n2)
    elif opcao == '3':
        print("Resultado:", n1 * n2)
    elif opcao == '4':
        if n2 != 0:
            print("Resultado:", n1 / n2)
        else:
            print("Erro: divisão por zero.")
    else:
        print("Opção inválida.")
