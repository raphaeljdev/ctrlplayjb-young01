soma = 0

while True:
    n = int(input("Digite um número (0 para parar): "))
    if n == 0:
        break
    soma += n

print("Soma total =", soma)
