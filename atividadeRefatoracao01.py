# Variaveis de preço
p1 = 100
p2 = 200
p3 = 300

t = p1 + p2 + p3

desc = 0
if t > 500:
    desc = t * 0.1

r = t - desc

print("Total antes do desconto:",t)
print("Desconto aplicado:", desc)
print("Total com desconto:", r)