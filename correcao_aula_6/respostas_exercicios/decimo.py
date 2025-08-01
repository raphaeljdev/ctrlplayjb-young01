frase = "python é uma linguagem de programação poderosa e versátil python é ótima"
palavras = frase.split() # Divide a frase em uma lista de palavras
frequencia = {} # Dicionário para armazenar a contagem

for palavra in palavras:
    # Se a palavra ainda não está no dicionário, adiciona com valor 1
    if palavra not in frequencia:
        frequencia[palavra] = 1
    # Se já existe, incrementa o valor
    else:
        frequencia[palavra] += 1

print(frequencia)