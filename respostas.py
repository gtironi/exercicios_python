# Questão 1

def converter_lista_para_string (lista):
    frase = ""
    for letra in lista:
        frase += letra
    frase = frase.replace("/", " ")
    titulo = frase.title()
    return titulo

# Questão 2

def pares_e_impares(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero%2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    pares.sort()
    impares.sort()
    resultado = []
    resultado.append(pares)
    resultado.append(impares)
    return resultado


# Questão 3

def cria_matriz(linhas, colunas):


# Questão 4

def filtrar_palavras(frase, letra):


# Questão 5

def eh_perfeito(numero):


