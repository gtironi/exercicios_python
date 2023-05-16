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

# print(remove_duplicados(dc))

# -------------------------------------------------------------

# controle de pedidos restaurante (tipo mcdonalds)

def adicionar_pedido(numero_do_pedido, fila_de_pedidos):
    fila_de_pedidos.append(numero_do_pedido)
    print(f"Pedido {numero_do_pedido} adicionado")

def preparar_pedidos(fila_de_pedidos):
    fila_de_pedidos.pop(0)
    print(f"Pedido {fila_de_pedidos[0]} está pronto")

def listar_pedidos_em_preparo(fila_de_pedidos):
    for pedido in fila_de_pedidos:
        print (f"Preparando {pedido}")

def verificar_pedido(numero_do_pedido, fila_de_pedidos):
    if numero_do_pedido in fila_de_pedidos:
        print(f"Seu pedido é o {fila_de_pedidos.index(numero_do_pedido)+1}º na lista")
    else:
        print("Esse pedido não está na lista")
        return

pedidos_em_preparo = []


adicionar_pedido(1, pedidos_em_preparo)
adicionar_pedido(2, pedidos_em_preparo)
adicionar_pedido(3, pedidos_em_preparo)
listar_pedidos_em_preparo(pedidos_em_preparo)
preparar_pedidos(pedidos_em_preparo)
adicionar_pedido(4, pedidos_em_preparo)
preparar_pedidos(pedidos_em_preparo)
adicionar_pedido(5, pedidos_em_preparo)
listar_pedidos_em_preparo(pedidos_em_preparo)
verificar_pedido(5, pedidos_em_preparo)



        
