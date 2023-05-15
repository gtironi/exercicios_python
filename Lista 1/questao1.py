def converter_lista_para_string (lista):
    frase = ""
    for letra in lista:
        frase += letra
    frase = frase.replace("/", " ")
    titulo = frase.title()
    return titulo



x= converter_lista_para_string(["e", "s", "q", "u", "e", "c", "e", "r", "a", "m", "/", "d", "e", "/", "m", "i", "m"])

print (x)
