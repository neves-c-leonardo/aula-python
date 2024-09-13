alunos = {"leonardo": 80, "brenda": 95, "catarina": 100}

def recuperarNotaAluno(aluno):
    if aluno in alunos:
        print(f"O aluno {aluno} está com nota: {alunos[aluno]}")
    else:
        print("Aluno não encontrado! Tente novamente")

        operacao = input("Deseja tentar novamente? (S/N) ")
        if operacao.upper() == "S":
            main()
        elif operacao.upper() == "N":
            print("Programa finalizado!")
        else:
            print("Operação não reconhecida! O programa irá finalizar!")
        

def main():
    aluno = input("Digite o nome do aluno que deseja consultar a nota: ")
    recuperarNotaAluno(aluno)

main()   
