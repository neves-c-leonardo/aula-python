import random

# Função para gerar uma lista de números aleatórios
def gerar_lista(tamanho):
    return [random.randint(1, 100) for _ in range(tamanho)]

# Função para adicionar um número à lista
def adicionar_numero(lista, numero):
    lista.append(numero)

# Função para remover um número da lista
def remover_numero(lista, numero):
    try:
        lista.remove(numero)
    except ValueError:
        print(f"O número {numero} não está na lista.")

# Função para exibir a lista
def exibir_lista(lista):
    print("Lista atual:", lista)

# Função para calcular a soma da lista
def soma_lista(lista):
    return sum(lista)

# Função para calcular a média da lista
def media_lista(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

# Função principal para interagir com o usuário
def main():
    lista_numeros = gerar_lista(10)
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar número")
        print("2. Remover número")
        print("3. Exibir lista")
        print("4. Calcular soma")
        print("5. Calcular média")
        print("6. Sair")
        
        opcao = input("Digite sua opção: ")
        
        if opcao == '1':
            numero = int(input("Digite o número a ser adicionado: "))
            adicionar_numero(lista_numeros, numero)
        elif opcao == '2':
            numero = int(input("Digite o número a ser removido: "))
            remover_numero(lista_numeros, numero)
        elif opcao == '3':
            exibir_lista(lista_numeros)
        elif opcao == '4':
            print("Soma da lista:", soma_lista(lista_numeros))
        elif opcao == '5':
            print("Média da lista:", media_lista(lista_numeros))
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
