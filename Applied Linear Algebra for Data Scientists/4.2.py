#4.2

'''

Создайте переменную, содержащую целые числа от 0 до 3, 
и вторую переменную, равную первой переменной плюс некоторое смещение.
Затем создайте симуляцию, в которой вы систематически варьируете 
это смещение между –50 и +50 (то есть на первой итерации симуляции вторая 
переменная будет равна [–50, –49, –48, –47]). В цикле for вычислите корре-
ляцию и косинусное сходство между двумя переменными и сохраните эти 
результаты. Затем постройте линейный график, показывающий, как среднее 
смещение влияет на корреляцию и косинусное сходство.

'''

import matplotlib.pyplot as plt

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
        return 0
    
    return covariance / (std_x * std_y)

def cosine_similarity(x, y):
    if len(x) != len(y):
        raise ValueError("Длины векторов должны быть одинаковыми")
    
    dot_product = sum(xi * yi for xi, yi in zip(x, y))
    
    magnitude_x = sum(xi ** 2 for xi in x) ** 0.5
    magnitude_y = sum(yi ** 2 for yi in y) ** 0.5
    
    if magnitude_x == 0 or magnitude_y == 0:
        return 0
    
    return dot_product / (magnitude_x * magnitude_y)

a = [0, 1, 2, 3]
pearson = []
cosinus = []

bias = [i for i in range (-50, 51)]

for b in bias:
    shifted_a = [x + b for x in a]
    
    p = pearson_correlation(a, shifted_a)
    c = cosine_similarity(a, shifted_a)

    pearson.append(p)
    cosinus.append(c)

plt.figure(figsize=(10, 6))
plt.plot(bias, pearson, label='Корреляция Пирсона')
plt.plot(bias, cosinus, label='Косинусное сходство')
plt.xlabel('Смещение')
plt.ylabel('Значение метрики')
plt.title('Зависимость корреляции и косинусного сходства от смещения')
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.axvline(0, color='black', linestyle='--', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()
