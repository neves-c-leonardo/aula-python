alunos = {"leonardo": 80, "brenda": 95, "catarina": 100}

def recuperarNotaAluno(aluno):
    try:
        if aluno in alunos:
            print(f"O aluno {aluno} está com nota: {alunos[aluno]}")
        else:
            raise KeyError
    
    except KeyError:
        print("Aluno não encontrado! Tente novamente")

        operacao = input("Deseja tentar novamente? (S/N) ")
        if operacao.upper() == "S":
            main()
        elif operacao.upper() == "N":
            print("Programa finalizado!")
        else:
            raise ValueError("Operação não reconhecida!") 
                
    except ValueError as ve:
        print(ve)
        

def main():
    try:
        aluno = input("Digite o nome do aluno que deseja consultar a nota: ")
        recuperarNotaAluno(aluno)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

main()   
