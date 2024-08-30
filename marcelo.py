# estaEspera = input("Você est´na lsta de Espera? (Sim/Não)")
# if(estaEspera.upper() == "SIM"):
#     emListaEspera = True
# elif(estaEspera.upper() == "NAÕ" or estaEspera.upper() == "NÃO"):
#     emListaEspera = False
# else:
#     print("Não foi digitado corretamente a pergunta da lista de espera!")
    

def validarInscricao(nome, dia, idade, indicacao, emEspera):
    diaMaxInscricao = 28
    idadeMax = 17
    idadeMin = 14

    if dia <= diaMaxInscricao or indicacao:
        if idade >= idadeMin and idade <= idadeMax:
            print(f"{nome} está apto por idade")
        else:
            print(f"{nome} não esta apto por idade!")
            return False
        if not emEspera:
            print(f"{nome} não está na lista de espera")
        else:
            print(f"{nome} esta na lista de espera")
            return False
        return True
    else:
        print("Inscrição não liberada")
        return False
    

emListaEspera = False
indicacao = True
diaAtual = 29
idadeCandidato = 15

inscricao = validarInscricao("Marcelo", diaAtual, idadeCandidato, indicacao, emListaEspera)
if(inscricao):
    print("Marcelo foi inscrito no campeonato!")
else:
    print("Não foi possivel fazer sua inscrição")

emListaEspera = True
indicacao = False
diaAtual = 27
idadeCandidato = 16

inscricao = validarInscricao("Fulano", diaAtual, idadeCandidato, indicacao, emListaEspera)
if(inscricao):
    print("Fulano foi inscrito no campeonato!")
else:
    print("Não foi possivel fazer sua inscrição")