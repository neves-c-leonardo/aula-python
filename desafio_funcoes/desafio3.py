def manipularString(texto):

    textoMaisculo = texto.upper()
    textoMinusculo = texto.lower()
    totaisCaracteres = len(texto)

    return (textoMaisculo, textoMinusculo, totaisCaracteres)


def main():
    palavra = input("Digite uma string para ser manipulada: ")

    resultadoMaisuculo, resultadoMinusculo, resultadoTotaisCaracteres = manipularString(palavra)

    print(f"Sua palavra em maisculo: {resultadoMaisuculo}")
    print(f"Sua palavra em minusculo: {resultadoMinusculo}")
    print(f"Totais de caracteres da sua palavra: {resultadoTotaisCaracteres}")
    
main()