def celsius_para_fahrenheit(celsius):
  """
    Converte a temperatura de Celsius para Fahrenheit.\n
    Input: celsius (float): Temperatura em graus Celsius.\n
    Output: Temperatura em graus Fahrenheit (float).
  """
  return (celsius * 9/5)

def fahrenheit_para_celsius(fahrenheit):
  """
    Converte a temperatura de Fahrenheit para Celsius.\n
    Input: fahrenheit (float): Temperatura em graus Fahrenheit.\n
    Output: Temperatura em graus Celsius (float).
  """
  return (fahrenheit - 32) * 5/9

def main():
  print("Bem-vindo ao conversor de temperatura!")
  escolha = input("Você deseja converter de Celsius para Fahrenheit (digite 'C') ou de Fahrenheit para Celsius (digite'F'): ").strip().upper()

  if escolha.upper() == 'C':
    temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
    temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
    print(f"{temperatura_celsius:.3f}°C é igual a {temperatura_fahrenheit:.3f}°F.")

  elif escolha.upper() == 'F':
    temperatura_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    temperatura_celsius = fahrenheit_para_celsius(temperatura_fahrenheit)
    print(f"{temperatura_fahrenheit:.2f}°F é igual a {temperatura_celsius:.2f}°C.")

  else:
    print("Opção invalida! Utilize 'C' ou 'F' para realizar a conversão")
    main()

main()

