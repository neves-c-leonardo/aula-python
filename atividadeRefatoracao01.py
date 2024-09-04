# Variaveis de preço
preco_produtos = [100, 200]

total_preco = sum(preco_produtos)

print(f"Total Preço: {total_preco}")

# Aplica um desconto de 10% se o total dos preços exceder 500
if total_preco > 500:
    desconto = (total_preco * 0.1)
    total_com_desconto = total_preco - desconto
    print(f"Desconto aplicado: {desconto}")
    print(f"Total com desconto: {total_com_desconto}" )
else:
    diferenca = 500 - total_preco
    print(f"Faltou {diferenca} para o desconto ser aplicado! Deseja incluir mais produtos?")