a = 5
b = 3

## igualdade
resultado = a == b
print(resultado)

## Diferença
resultado = a != b
print(resultado)

# Maior que (>)
resultado = a > b
print(resultado)

# Menor que (<)
resultado = a < b
print(resultado)

# Maior ou igual (>=)
resultado = a >= b
print(resultado)

# Menor ou igual (<=)
resultado = a <= b
print(resultado)


##  Ana está organizando uma festa do dia 26 e comprou os seguintes itens:
# Pizzas: 8 unidades
# Bebidas (em litros): 15 litros
# Bolos: 3 unidades
# Doces (em gramas): 500 gramas

# As quantidades mínimas necessárias são:
# Pizzas: no mínimo 10 unidades
# Bebidas: no mínimo 12 litros
# Bolos: no mínimo 5 unidades
# Doces: no mínimo 600 gramas

## Objetivo: Verificar se as quantidades compradas atendem ou 
# excedem as necessidades mínimas e identificar quais itens 
# estão abaixo da quantidade mínima.

dia = int(input("Qual o dia de hoje? "))
pedidoPizza = int(input("Quantas pizzas comprou? "))
pedidoBebida = int(input("Quantas bebidaS comprou? "))
pedidoBolo = int(input("Quantas bolos comprou? "))
pedidoDoce = int(input("Quantas doces comprou? "))
#  Declarando variaveis
diaFesta = 26
pedidoMinimoPizza = 10
pedidoMinimoBebida = 12
pedidoMinimoBolo = 5
pedidoMinimoDoce = 600

if diaFesta == dia:
    print("Ana esta fazendo as compras no dia da festa!")
else:
    print("Ana esta fazendo compra adianta")

if(pedidoMinimoPizza >= pedidoPizza):
    if(pedidoMinimoPizza == pedidoPizza):
        print("Ana comprou o minimo permitido de pizza")
    print("Ana não comprou pizzas suficientes!")

if(pedidoMinimoBebida < pedidoBebida):
    print("Ana comprou mais bebidas que o necessário!")

if(pedidoMinimoBolo < pedidoBolo):
    print("Ana excedeu a compra de bolos!")
elif(pedidoMinimoBolo == pedidoBolo):
    print("Ana comprou o minimo permitido de bolo")
else:
    print("Ana não comprou bolos suficiente")

if(pedidoMinimoDoce > pedidoDoce):
    print("Ana não comprou doces suficiente")