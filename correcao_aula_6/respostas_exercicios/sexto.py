frutas = {"maçã", "banana", "uva"}

fruta_digitada = input("Digite o nome de uma fruta: ")

if fruta_digitada.lower() in frutas:
    print("A fruta está na lista!")
else:
    print("Fruta não encontrada.")