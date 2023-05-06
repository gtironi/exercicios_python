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

def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)
    numero = 1
    for i in range(num_linhas):
        for j in range(num_colunas):
            matriz[i][j] = numero
            numero += 1
    return matriz

# Questão 4

def filtrar_palavras(frase, letra):
    lista = []
    palavras = frase.split()
    for palavra in palavras:
        if palavra.count(letra) > 0 or palavra.count(letra.upper()):
            lista.append(palavra)
    return lista

# Questão 5

def eh_perfeito(numero):
    return 1

