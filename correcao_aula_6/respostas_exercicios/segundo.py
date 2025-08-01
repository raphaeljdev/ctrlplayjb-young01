coordernada = (10, 20)
escolha_do_usuario = input("Escolha entre X ou Y: ")
if escolha_do_usuario.lower() == "x":
    print(coordernada[0])
elif escolha_do_usuario.lower() == "y":
    print(coordernada[1])
else:
    print("Opção inválida.")