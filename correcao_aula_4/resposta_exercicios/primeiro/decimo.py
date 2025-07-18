valor = float(input("Valor da compra: "))
vip = input("Cliente é VIP? (sim/não): ").lower()

if vip == "sim" and valor > 100:
    desconto = 0.20
else:
    desconto = 0.10

valor_final = valor * (1 - desconto)

print(f"Desconto aplicado: {int(desconto * 100)}%")
print("Valor final:", round(valor_final, 2))
