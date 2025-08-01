dia1 = {"mouse", "teclado", "monitor", "cabo HDMI"}
dia2 = {"teclado", "mousepad", "webcam", "cabo HDMI"}

# 1. Interseção: produtos vendidos em ambos os dias
vendidos_ambos_dias = dia1.intersection(dia2)
print(f"Produtos vendidos em ambos os dias: {vendidos_ambos_dias}")

# 2. União: todos os produtos únicos vendidos
todos_produtos_vendidos = dia1.union(dia2)
print(f"Todos os produtos vendidos (sem repetição): {todos_produtos_vendidos}")

# 3. Diferença: produtos vendidos no dia 1, mas não no dia 2
vendidos_apenas_dia1 = dia1.difference(dia2)
print(f"Produtos vendidos apenas no dia 1: {vendidos_apenas_dia1}")