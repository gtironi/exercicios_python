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




print(cria_matriz(2,3))

