import numpy as np

# a1D_1 = np.array([1,2,3,4])
# a1D_2 = np.array([5,6,7,8])

# a1D = np.concatenate((a1D_1, a1D_2))

# print(a1D[4])

# print(a1D{2:6:2})

# (type(a1D))

# print(f'''Dados de um a1D:
# Dimensão: {a1D.ndim}
# Tamanho: {a1D.size}
# Tipo: {a1D.dtype}
# Tamanho do elemento: {a1D.itemsize}''')

a2D =  np.array([[1.0, 2.0], [3.0, 4.0]])

print(f'''Dados de um a1D:
Dimensão: {a2D.ndim}
Tamanho: {a2D.size}
Tipo: {a2D.dtype}
Tamanho do elemento: {a2D.itemsize}
Forma do a2D: {a2D.shape}''')

print(a2D[0, 0])

print(a2D[::-1,::-1])
