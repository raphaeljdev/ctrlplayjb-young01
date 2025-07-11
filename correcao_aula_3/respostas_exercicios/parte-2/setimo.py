p1 = input("Palavra 1: ")
p2 = input("Palavra 2: ")
p3 = input("Palavra 3: ")

palavras = [p1, p2, p3]

if p1 == p2 or p1 == p3 or p2 == p3:
    print("Você digitou palavras repetidas.")
else:
    print("Todas as palavras são diferentes.")
