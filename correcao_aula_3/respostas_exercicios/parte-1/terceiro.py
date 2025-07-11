frutas = ["maçã", "banana", "uva"]
remover = input("Qual fruta você quer remover da lista? ")

if remover in frutas:
    frutas.remove(remover)
    print("Fruta removida com sucesso!")
else:
    print("Essa fruta não está na lista.")

print("Lista atual de frutas:", frutas)
