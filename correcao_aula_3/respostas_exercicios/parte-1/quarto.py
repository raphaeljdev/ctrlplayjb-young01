n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

numeros = [n1, n2, n3]
numeros.insert(1, 100)

print("Lista após inserção de 100 na segunda posição:", numeros)
