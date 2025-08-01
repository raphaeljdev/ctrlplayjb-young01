agenda = {}

while True:
    print("\n--- Agenda ---")
    opcao = input("O que deseja fazer? (adicionar, ver, sair): ").lower()

    if opcao == 'adicionar':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        agenda[nome] = telefone
        print(f"Contato {nome} adicionado!")
    
    elif opcao == 'ver':
        if not agenda: # Verifica se o dicionário está vazio
            print("A agenda está vazia.")
        else:
            print("\n--- Contatos ---")
            for nome, telefone in agenda.items():
                print(f"Nome: {nome}, Telefone: {telefone}")

    elif opcao == 'sair':
        print("Saindo da agenda...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")