def celsius_a_fahrenheit(celsius):
  """Convierte grados Celsius a Fahrenheit."""
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
  """Convierte grados Fahrenheit a Celsius."""
  celsius = (fahrenheit - 32) * 5/9
  return celsius

# Solicitar al usuario la temperatura y la unidad de medida
temperatura = float(input("Ingrese la temperatura: "))
unidad = input("Ingrese la unidad de medida (C/F): ").upper()

# Convertir la temperatura según la unidad ingresada
if unidad == "C":
  resultado = celsius_a_fahrenheit(temperatura)
  unidad_salida = "F"
elif unidad == "F":
  resultado = fahrenheit_a_celsius(temperatura)
  unidad_salida = "C"
else:
  print("Unidad no válida.")
  exit()

# Mostrar el resultado
print(f"{temperatura:.2f}°{unidad} es equivalente a {resultado:.2f}°{unidad_salida}")