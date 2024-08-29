a = 5
b = 3
c = 4

# Adição (+)
resultado = a + b + c
print(f"Soma: {resultado}")

#Subtração (-)
resultado = c - b
print(f"Subtração: {resultado}")

# Multiplicação
resultado = b * a
print(f"Multiplicação: {resultado}")

# Divisão
resultado = a / b
print(f"Divisão: {resultado}")

# Divisão Inteira
resultado = a // b
print(f"Divisão Inteira: {resultado}")

# Resto da divisão (%)
resultado = a % b
print(f"Resto da divisão: {resultado}")

#Exponencial(**)
resultado = a ** b
print(f"Exponencial: {resultado}")

##José foi ao mercado com R$ 50,00. Ele comprou:
# - 2 refrigerantes R$ 8,00/cada
# - 3 pães R$ 4,00
# - 300g de mortadela (Valor do quilo de mortadela R$ 39,90)
# Após as compras, José deseja saber quanto 
# sobrou de seu dinheiro e se há algum valor 
# exato que ele poderia gastar com os trocados restantes.

# Declarando variavel
saldoInicial = 50
custoRefrigerante = 8
custoPao = 4
custoMortadela = 39.90

valorCompra = (custoRefrigerante * 2) + custoPao + ((custoMortadela / 1000) * 300)

saldoFinal = saldoInicial - valorCompra
print(f"José chegou com R${saldoInicial} e saiu com R${saldoFinal}")

