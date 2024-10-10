# Variaveis Globais
idade = int(input("Qual é a sua idade? "))

# No trecho de condição será validado a idade da persona para analisar sua categproa
def validarIdadePersona(idade):
    mensagemPadrao = "A pessoa é classificada como: "
    if idade < 0:
        return "Essa pessoa por acaso ja nasceu?"
    elif idade > 0 and idade <= 2:
        return mensagemPadrao + "Bebê!"
    elif idade > 2 and idade < 13:
        return mensagemPadrao + "Criança!"
    elif idade >= 13 and idade < 18:
        return mensagemPadrao + "Adolescente!"
    elif idade >= 18 and idade <= 60:
        return mensagemPadrao + "Adulto!"
    elif idade > 60 and idade <= 105:
        return mensagemPadrao + "Idoso!"
    else:
        return "Alguem verifica se ainda ta vivo?!"

categoriaIdade = validarIdadePersona(idade) 
print(categoriaIdade)