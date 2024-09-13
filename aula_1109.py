# Método de Busca Leitura
with open("text/exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Método de Busca Escrever
with open("text/exemplo2.txt", 'w', encoding='utf-8') as arquivo:
    arquivo.write("Olá!")
    arquivo.write("Mundoo!")

# Método de Acrescentar
with open("text/exemplo.txt", 'a', encoding='utf-8') as arquivo:
    arquivo.write("\nTexto adicional")