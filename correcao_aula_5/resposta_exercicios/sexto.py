total = 0
qtd = int(input("Quantos produtos? "))

for i in range(qtd):
    preco = float(input(f"Preço do produto {i+1}: "))
    if preco > 100:
        preco *= 0.9  # 10% desconto
    elif preco > 50:
        preco *= 0.95  # 5% desconto
    total += preco

print(f"Total com descontos: R${total:.2f}")
