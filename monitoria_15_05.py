biblioteca = {}

def novo_livro(**dados):
    livro ={}
    for chave, valor in dados.items():
        chave = chave.title()
        if type(valor) == str:
            valor = valor.title()
        livro[chave] = valor

    return livro

def adicionar_livro(biblioteca, *livros):
    for livro in livros:
        titulo = livro.get("Titulo")
        livro.pop("Titulo")
        biblioteca[titulo] = livro

l1 = novo_livro(titulo = "sapiens", ano = 1980, autor = "iuri")
l2 = novo_livro(titulo = "diario de um banana", ano = 1873, genero = "infantil")

adicionar_livro(biblioteca, l1, l2)

print(biblioteca)

# -----------------------------------------------

def analise_estatistica(*valores):
    soma = 0
    lista = list(valores)
    medidas_resumo = {}
    soma = sum(lista)
    lista.sort
    quantidade_numeros = int(len(lista))
    if quantidade_numeros%2 == 0:
        x=quantidade_numeros/2
        mediana = (lista[int(x)] + lista[int(x-1)])/2
    else:
        x=(quantidade_numeros+1)/2
        mediana = lista[int(x-1)]
    media =  soma/quantidade_numeros
    lista_unica = list(set(lista))
    dict_quanti_num = {}
    for numero in lista_unica:
        dict_quanti_num[numero] = lista.count(numero)
    moda = max(dict_quanti_num, key=dict_quanti_num.get)

    return media, mediana, moda

print(analise_estatistica(1,1,1,1,2,4,6,8,8,8,8,8,10))

