# min e max dicionario

dc = {"Joao": 10, "Carlos": 20, "Maria": 25, "Antonio": 20}

def min_max_dicionario(dict):
    valores = list(dict.values())
    min = valores[0]
    max = valores[0]
    for numero in valores:
        if numero > max:
            max = numero
        elif numero < min:
            min = numero
    return min, max

# print(min_max_dicionario(dc))

# -------------------------------------------------------------

# n primeiros quadrados

def numeros_quadrados(n):
    dicionario = dict()
    for i in range(1, n+1):
        dicionario[i] = i**2
    return dicionario

# print(numeros_quadrados(5))

# -------------------------------------------------------------

# remove os valores duplicados do dicionario com loop

# def remove_duplicados(dicio):
#     dicio_novo = dict()
#     lista = []
#     chaves = list(dicio)
#     for chave in chaves:
#         if dicio[chave] not in lista:
#             dicio_novo[chave] = dicio[chave]
#         lista.append(dicio[chave])
#     return dicio_novo

def remove_duplicados(dicio):
    lista = []
    chaves = list(dicio)
    for chave in chaves:
        if dicio[chave] in lista:
            del dicio[chave]
        else:
            lista.append(dicio[chave])
    return dicio

print(remove_duplicados(dc))



        