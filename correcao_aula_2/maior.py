# Verificar qual é o maior entre dois números

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    print("O primeiro número é maior.")
elif b > a:
    print("O segundo número é maior.")
else:
    print("Os dois números são iguais.")
