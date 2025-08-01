num = int(input("Digite um número inteiro: "))
eh_primo = True # Flag para controlar se é primo

# 0 e 1 não são primos
if num < 2:
    eh_primo = False
else:
    # Verifica divisores de 2 até a raiz quadrada do número (otimização)
    # ou simplesmente até o próprio número.
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            eh_primo = False # Encontrou um divisor, então não é primo
            break # Já podemos parar

if eh_primo:
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")