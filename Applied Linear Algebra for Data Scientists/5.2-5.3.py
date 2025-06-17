'''

Упражнение 5.2
Это и следующее упражнения сосредоточены на нарезке матриц с целью 
получения подматриц. Начните с  создания матрицы C на рис. 5.6 и  при-
мените существующую в Python операцию нарезки, чтобы извлечь подматрицу,
состоящую из первых пяти строк и  пяти столбцов. Давайте назовем 
эту матрицу C1. Попробуйте воспроизвести рис. 5.6, но если у вас возникли 
проблемы с программированием визуализации на Python, то просто сосре-
доточьтесь на правильном извлечении подматрицы.

Упражнение 5.3
Расширьте этот исходный код, чтобы извлечь остальные четыре блока 
размером 5×5. Затем создайте новую матрицу с  этими блоками.

'''

import numpy as np

matrix = np.arange(100).reshape(10, 10)

def extract_submatrix(matrix, start_row, end_row, start_col, end_col):
    return [row[start_col:end_col + 1] for row in matrix[start_row:end_row + 1]]

sub_matrix_1 = extract_submatrix(matrix, 0, 4, 0, 4)
sub_matrix_2 = extract_submatrix(matrix, 0, 4, 5, 9)
sub_matrix_3 = extract_submatrix(matrix, 5, 9, 0, 4)
sub_matrix_4 = extract_submatrix(matrix, 5, 9, 5, 9)

new_matrix = np.vstack([
    np.hstack([sub_matrix_4, sub_matrix_3]),
    np.hstack([sub_matrix_2, sub_matrix_1])
])

print(new_matrix)