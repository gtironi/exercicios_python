import numpy as np
import numpy.random as npr

#Operações em NDArrays

print("#"*60)

a1D_1 = np.arange(10)
print(a1D_1, end='\n\n')

a1D_1 = a1D_1.reshape(5,2)
print(a1D_1, end='\n\n')

a1D_1 = a1D_1.transpose()
print(a1D_1, end='\n\n')

print("#"*60)

a1D_2 = np.arange(20)
print(a1D_2, end='\n\n')

a1D_2 = a1D_2.reshape(10,2)
print(a1D_2, end='\n\n')

a1D_3 = np.vstack((a1D_2, a1D_2))
print(a1D_3, end='\n\n')

a1D_3 = np.hstack((a1D_2, a1D_2))
print(a1D_3, end='\n\n')

print(f"Dados sobre a1D_3: \n\t\
Dimensão: {a1D_3.ndim} \n\t\
Forma: {a1D_3.shape} \n")

print("#"*60)

#Shallow Copy

a1D = np.arange(10)
print(a1D)

a1D_copy = a1D
print(a1D_copy, '\n')

a1D_copy[0] = 42
print(a1D)
print(a1D_copy, '\n')

print(id(a1D))
print(id(a1D_copy), '\n')

print("#"*60)

#Deep Copy

a1D = np.arange(10)
print(a1D)

a1D_copy = a1D.copy()
print(a1D_copy, '\n')

a1D_copy[0] = 42
print(a1D)
print(a1D_copy, '\n')

print(id(a1D))
print(id(a1D_copy), '\n')

print("#"*60)

a1D = np.arange(10)

outro_vetor = a1D.reshape(5,2)
print(id(outro_vetor))

outro_vetor[0, 0] = 42

print(a1D)
print(outro_vetor, '\n')

print(id(a1D))
print(id(outro_vetor), '\n')

print("#"*60)

zeros = np.zeros(42,  dtype=np.int64)
print(zeros, '\n')

uns = np.ones(42,  dtype=np.int64)
print(uns, '\n')

identidade = np.identity(5, dtype=np.int64)
# identidade = np.eye(5, dtype=np.int64)
print(identidade, '\n')

numeros = np.array([n for n in range(7,43)])
# numeros = np.arange(7, 43)
print(numeros, '\n')

pares = np.arange(8, 43,2)
print(pares, '\n')

numero = npr.rand(1)
print(numero, '\n')

amostra_numeros = npr.randn(10)
print(amostra_numeros, '\n')

quarenta_e_dois = np.ones(10, dtype=np.int64) * 42
print(quarenta_e_dois, '\n')

matriz_aleatorio = npr.randint(1, 10, 9).reshape(3,3)
print(matriz_aleatorio)
