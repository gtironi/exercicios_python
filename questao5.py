def divisores(numero):
    lista_divisores = []
    for i in range(1, int(numero/2+1)):
        if numero % i == 0: 
           lista_divisores.append(i)
    return lista_divisores

def eh_perfeito(numero):
    soma = sum(divisores(numero))
    if soma == numero:
        return True
    else:
        return False

print(eh_perfeito(0))


    