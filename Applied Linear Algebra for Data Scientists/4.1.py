#4.1

'''

Напишите функцию Python, которая на входе принимает два вектора и на 
выходе выдает два числа: коэффициент корреляции Пирсона и  значение 
косинусного сходства. Напишите исходный код, который следует форму-
лам, представленным в данной главе; не используйте вызовы встроенной 
в NumPy функции np.corrcoef и встроенной в SciPy функции spatial.distance.
cosine. Убедитесь, что два значения на выходе идентичны, когда переменные 
уже центрированы по среднему значению, и различны, когда переменные не 
центрированы по среднему значению.

'''

def pearson_correlation(x, y):
    n = len(x)
    if n != len(y):
        raise ValueError("Длины массивов должны быть одинаковыми")
    
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    covariance = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    std_x = sum((xi - mean_x) ** 2 for xi in x) ** 0.5
    std_y = sum((yi - mean_y) ** 2 for yi in y) ** 0.5
    
    if std_x == 0 or std_y == 0:
        return 0  # Если одно из отклонений нулевое, корреляция не определена
    
    return covariance / (std_x * std_y)

def cosine_similarity(x, y):
    if len(x) != len(y):
        raise ValueError("Длины векторов должны быть одинаковыми")
    
    dot_product = sum(xi * yi for xi, yi in zip(x, y))
    magnitude_x = sum(xi ** 2 for xi in x) ** 0.5
    magnitude_y = sum(yi ** 2 for yi in y) ** 0.5
    
    if magnitude_x == 0 or magnitude_y == 0:
        return 0  # Если один из векторов нулевой, сходство не определено
    
    return dot_product / (magnitude_x * magnitude_y)

def center_vector(a, b):
    mean_a = sum(a) / len(a)
    mean_b = sum(b) / len(b)
    return [ai - mean_a for ai in a], [bi - mean_b for bi in b]

# Пример использования с нецентрированными данными
x = [1, 2, 3]
y = [4, 5, 6]

print("Нецентрированные данные:")
print("Корреляция Пирсона:", pearson_correlation(x, y))
print("Косинусное сходство:", cosine_similarity(x, y))

# Центрируем данные
x_centered, y_centered = center_vector(x, y)

print("\nЦентрированные данные:")
print("Корреляция Пирсона:", pearson_correlation(x_centered, y_centered))
print("Косинусное сходство:", cosine_similarity(x_centered, y_centered))
