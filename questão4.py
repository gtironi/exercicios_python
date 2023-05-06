def filtrar_palavras(frase, letra):
    lista = []
    palavras = frase.split()
    for palavra in palavras:
        if palavra.count(letra) > 0 or palavra.count(letra.upper()):
            lista.append(palavra)
    return lista


print(filtrar_palavras("Alo, galera de carro, ai que vai", "a"))