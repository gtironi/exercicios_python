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