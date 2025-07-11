f1 = input("Fruta 1: ")
f2 = input("Fruta 2: ")
f3 = input("Fruta 3: ")

frutas = [f1, f2, f3]
verificar = input("Qual fruta você quer verificar? ")

if verificar in frutas:
    print("Está na lista!")
else:
    print("Não está na lista!")
