# numero = int(input("Digite um numero: "))

def funcaoComTry():
    try:
        n1 = int(input("Digite um numero: "))
        numero = 2 / 0
    except ZeroDivisionError as z:
        print("funcaoComTry :: Não é possivel dividr por zero!")
    except Exception as e:
        print(f"funcaoComTry :: Erro no trecho do código {e}")


funcaoComTry()