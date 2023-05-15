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
