# min e max dicionario
dc = {"Joao": 10, "Carlos": 20, "Maria": 25}

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



