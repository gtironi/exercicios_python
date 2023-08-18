import numpy as np

'''
import time

### loop for

inicio_tempo_loop = time.time()

for i in range(100):
    vetor_loop = list(range(1, 100))
    for number in range(len(vetor_loop)):
        vetor_loop[number] = vetor_loop[number] ** 2
    
fim_tempo_loop = time.time()


print("Tempo de loop:", fim_tempo_loop - inicio_tempo_loop)

### Numpy

inicio_tempo_loop = time.time()

for i in range(100):
    vetor_numpy = np.array(range(1,100))
    vetor_numpy = vetor_numpy ** 2

fim_tempo_loop = time.time()

print("Tempo de loop:", fim_tempo_loop - inicio_tempo_loop)
'''

def calcular_quadrado(num):
    return num ** 2

vetor_numpy = list(range(1,11))

funcao_vetorizada = np.vectorize(calcular_quadrado)

print(funcao_vetorizada(vetor_numpy))