idade = 25

categoria = "Indefinida"
if idade < 13:
    categoria = "Criança"
elif idade >= 13 and idade < 18:
    categoria = "Adolescente"

print("A pessoa é classificada como: ", categoria)