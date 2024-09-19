def main():
    contatos = []

    print(f"Minha lista de contatos atualmente tem {len(contatos)}")

    pessoaAlice = {"nome": "Alice", "telefone": "123-456-789"}
    pessoaBob = {"nome": "Bob", "telefone": "987-654-321"}

    contatos.append(pessoaAlice)
    print(f"Minha lista de contatos atualmente tem {len(contatos)}")
    print(f"Lista de contatos atualizada: {contatos}")

    contatos.append(pessoaBob)
    print(f"Minha lista de contatos atualmente tem {len(contatos)}")
    print(f"Lista de contatos atualizada: {contatos}")

main()
