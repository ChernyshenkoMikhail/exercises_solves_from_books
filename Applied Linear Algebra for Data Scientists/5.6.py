'''

Запрограммируйте умножение матриц с использованием циклов for. Под-
твердите свои результаты с помощью оператора @ библиотеки NumPy. Это 
упражнение поможет вам укрепить ваше понимание умножения матриц, но 
на практике всегда лучше использовать @ вместо написания двойного цикла 
for.

'''

import numpy as np

def matrix_multiply(A, B):

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

manual_result = matrix_multiply(A, B)
print("Результат:", manual_result)

A_np = np.array([[1, 2], [3, 4]])
B_np = np.array([[5, 6], [7, 8]])

numpy_result = A_np @ B_np
print("Результат NumPy (@):\n", numpy_result)

numpy_dot_result = np.dot(A_np, B_np)
print("Результат np.dot:\n", numpy_dot_result)