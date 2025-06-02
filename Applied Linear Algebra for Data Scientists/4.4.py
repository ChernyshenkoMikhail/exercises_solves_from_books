import numpy as np
from time import perf_counter

'''
Модифицируйте функцию из упражнения 4.2, чтобы вычислить только коэффициент корреляции.
Затем, в цикле for по 1000 итерациям, сгенерируйте две переменные из 500 случайных чисел
и вычислите корреляцию между ними. Засеките время исполнения цикла for.
Затем повторите, но используя функцию np.corrcoef.

'''

def pearson_correlation(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    cov = 0.0
    sum_sq_x = 0.0
    sum_sq_y = 0.0
    
    for xi, yi in zip(x, y):
        dx = xi - mean_x
        dy = yi - mean_y
        cov += dx * dy
        sum_sq_x += dx ** 2
        sum_sq_y += dy ** 2
    
    std_x = sum_sq_x ** 0.5
    std_y = sum_sq_y ** 0.5
    
    if std_x == 0 or std_y == 0:
        return 0.0
    
    return cov / (std_x * std_y)

n_iter = 1000
size = 50

# конкретно-прикладная функция
start = perf_counter()
for _ in range(n_iter):
    x = np.random.randn(size).tolist()
    y = np.random.randn(size).tolist()
    pearson_correlation(x, y)
py_time = perf_counter() - start
print(f"Оптимизированный Python: {py_time:.4f} сек")

# NumPy функция
start = perf_counter()
for _ in range(n_iter):
    x = np.random.randn(size)
    y = np.random.randn(size)
    np.corrcoef(x, y)[0, 1] # нужно указать [0, 1], чтобы возвращал число, а не матрицу в ndarray
numpy_time = perf_counter() - start
print(f"NumPy corrcoef: {numpy_time:.4f} сек")