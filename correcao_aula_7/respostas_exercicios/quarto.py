def celsius_para_fahrenheit(celsius):
  """Converte graus Celsius para Fahrenheit."""
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# Chamando a função
temp_c = 25
temp_f = celsius_para_fahrenheit(temp_c)
print(f"{temp_c}°C é igual a {temp_f}°F.")