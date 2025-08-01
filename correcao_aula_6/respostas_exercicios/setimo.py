precos = {
    "caderno": 20.00,
    "caneta": 3.00,
    "mochila": 150.00
}

# O método .items() retorna a chave e o valor a cada iteração
for produto, preco in precos.items():
    print(f"{produto.capitalize()}: R$ {preco:.2f}")