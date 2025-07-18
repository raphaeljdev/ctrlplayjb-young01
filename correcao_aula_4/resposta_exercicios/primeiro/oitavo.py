salario = float(input("Digite seu salário: "))

if salario < 2000:
    print("Isento de imposto")
elif salario <= 5000:
    print("Faixa de imposto: 10%")
else:
    print("Faixa de imposto: 20%")
