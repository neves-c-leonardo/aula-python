def calculadora(numero1, numero2, operacao):
  """
    Realiza uma operação matemática básica entre dois números.\n
    Input: numero1 (float): O primeiro número.\n
    Input: numero2 (float): O segundo número.\n
    Input: operacao (str): A operação matemática a ser realizada ('+', '-', '*', '/').\n
    Output: Temperatura em graus Fahrenheit (float).
  """
  if operacao == '+':
    return numero1 + numero2
  elif operacao == '-':
    return numero1 - numero2
  elif operacao == '*':
    return numero1 * numero2
  elif operacao == '/':
    if numero2 == 0:
      return "Erro: Divisão por zero não é permitida."
    return numero1 / numero2
 
def main():
  print("Bem-vindo à calculadora simples!")
 
  numero1 = float(input("Digite o primeiro número: "))
  numero2 = float(input("Digite o segundo número: "))

  operacao = input("Digite a operação desejada (+ para adição, - para subtração, * para multiplicação e / para divisão): ")

  if operacao not in ['+', '-', '*', '/']:
    print("Operação inválida!")
    novamente = input("Deseja tentar novamente? (S/N)").upper()

    if(novamente == "S"):
        main()
    else:
      print("Programa está sendo finalizado!")
      return

  resultado = calculadora(numero1, numero2, operacao)

  if isinstance(resultado, str):
    print(resultado)
  else:
    print(f"O resultado de {numero1} {operacao} {numero2} é {resultado:.2f}.")

main()


