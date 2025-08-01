n = int(input("Quantos termos da sequência de Fibonacci você quer gerar? "))

# Primeiros dois termos
a, b = 0, 1
contador = 0

if n <= 0:
    print("Por favor, digite um número positivo.")
elif n == 1:
    print(a)
else:
    print("Sequência de Fibonacci:")
    while contador < n:
        print(a, end=" ")
        # Calcula o próximo termo
        proximo_termo = a + b
        # Atualiza os valores para a próxima iteração
        a = b
        b = proximo_termo
        contador += 1