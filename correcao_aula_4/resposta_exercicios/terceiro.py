a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))

if a >= b and a >= c:
    print("O maior número é", a)
elif b >= a and b >= c:
    print("O maior número é", b)
else:
    print("O maior número é", c)
