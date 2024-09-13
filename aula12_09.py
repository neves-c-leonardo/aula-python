valor = ""

def saudacao(nome):
    """
        Função destinada a realizar saudação para uma pessoa!\n
        Input: nome (str) Nome da pessoa a ser saudada\n
        Output: print() com uma mensagem amigavel
    """
    valor = "Olá {nome}"


nome_pessoa = "Leonardo"
saudacao(nome_pessoa)
print(valor)


def comparar_numero_maior(a,b):
    if a > b:
        return True
    else:
        return False
    
if comparar_numero_maior(5,7):
    print("Número é maior")
else:
    print("Número é menor")
