palavra = input("Digite uma palavra (número par de letras): ")
meio = len(palavra) // 2
nova = palavra[:meio] + palavra[:meio-1:-1]
print(nova)
