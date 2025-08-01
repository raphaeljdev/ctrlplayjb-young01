soma_total = 0
numero = -1

print("Digite números para somar. Digite 0 para sair.")
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    soma_total += numero
print(soma_total)