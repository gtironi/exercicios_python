import numpy as np
import math
import numpy.random as npr

'''
lista_a = [1,2,3]
lista_b = [4,5,6]

a1D_a = np.array([1,2,3,4])
a1D_b = np.array([0,1,2,3])

print('Multiplicação:', a1D_a * a1D_b, '\n')

print('Multiplicação por inteiro:', a1D_a * 3, '\n')

print('Soma:',a1D_a + 3, '\n')

print('Subtração:', a1D_a - 3, '\n')

print('Exponencial:', a1D_a ** 3, '\n')

print('Divisão:', a1D_a / 3, '\n')
# print('Divisão por 0:', a1D_a / 0, '\n')

a1D_a = a1D_a.reshape(1,4)
a1D_b = a1D_b.reshape(4,1)

print(a1D_a)
print(a1D_b, '\n')

print(a1D_a * a1D_b, '\n')

ndarray = np.array([1,2,3,4,5,6])
indices = ndarray > 3

print(indices)
print(ndarray[indices], '\n')

indices = (ndarray%2 == 0)
print(ndarray[indices], '\n')

ndarray = np.arange(9).reshape(3,3)
indices = np.array([[False, True, False], [True, False, True], [True, True, True]])
print(ndarray, '\n')
print(indices, '\n')

print(ndarray[indices], '\n')
'''

notas = np.array([87, 72, 95, 93, 70, 100])

print('Average: ', np.average(notas) ,'\n')

print('Median: ', np.median(notas) ,'\n')

print('Standard Deviation: ', np.std(notas) ,'\n')

print('Minimun and Maximum: ', np.amin(notas), np.amax(notas),'\n')

print('Percentil: ', np.percentile(notas, 70),'\n')

print('Peak to Peak: ', np.ptp(notas),'\n')

























