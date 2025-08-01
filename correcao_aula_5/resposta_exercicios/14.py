n = int(input("Digite a altura da pirâmide: "))

# O loop externo controla o número de linhas
for i in range(1, n + 1):
    # O loop interno controla o número de asteriscos em cada linha
    # A linha 1 tem 1*, a linha 2 tem 2*, e assim por diante
    for j in range(i):
        print("*", end="")
    # Pula para a próxima linha depois de imprimir os asteriscos
    print() # Isso imprime uma nova linha