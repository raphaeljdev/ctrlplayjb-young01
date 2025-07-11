palavra = input("Digite uma palavra: ")
letras = [palavra[0], palavra[1], palavra[2], palavra[3], palavra[4]]

vogais = 0
if letras[0] in 'aeiouAEIOU':
    vogais += 1
if letras[1] in 'aeiouAEIOU':
    vogais += 1
if letras[2] in 'aeiouAEIOU':
    vogais += 1
if letras[3] in 'aeiouAEIOU':
    vogais += 1
if letras[4] in 'aeiouAEIOU':
    vogais += 1

print("Número de vogais:", vogais)
