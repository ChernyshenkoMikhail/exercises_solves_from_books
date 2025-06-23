'''

Подтвердите правило LIVE EVIL, выполнив следующие ниже пять шагов.
1.	 Создайте четыре матрицы случайных чисел, установив размеры L Î
ℝ2×6, I Î ℝ6×3, V Î ℝ3×5 и E Î ℝ5×2. 
2. Умножьте четыре матрицы и транспонируйте произведение. 
3.	 Транспонируйте каждую матрицу по отдельности и  умножьте их, не 
меняя их порядок следования. 
4.	 Транспонируйте каждую матрицу по отдельности и умножьте их в об-
ратном порядке в соответствии с правилом LIVE EVIL. Проверьте со-
впадение результата шага 2 с результатами шага 3 и шага 4. 
5.	 Повторите приведенные выше шаги, но используя только квадратные 
матрицы.

'''

#1
import numpy as np

np.random.seed(42)

L = np.random.rand(2, 6)
I = np.random.rand(6, 3)
V = np.random.rand(3, 5)
E = np.random.rand(5, 2)

#2
product = L @ I @ V @ E
transposed_product = product.T

print(transposed_product)

#3
L_T = L.T
I_T = I.T
V_T = V.T
E_T = E.T

wrong_order_result = L_T @ I_T @ V_T @ E_T
print(wrong_order_result)
print(np.allclose(transposed_product, wrong_order_result))

#4
live_evil_result = E_T @ V_T @ I_T @ L_T

print(live_evil_result)
print(np.allclose(transposed_product, live_evil_result))

#5
L_sq = np.random.rand(2, 2)
I_sq = np.random.rand(2, 2)
V_sq = np.random.rand(2, 2)
E_sq = np.random.rand(2, 2)

product_sq = L_sq @ I_sq @ V_sq @ E_sq
transposed_product_sq = product_sq.T

wrong_order_sq = L_sq.T @ I_sq.T @ V_sq.T @ E_sq.T

live_evil_sq = E_sq.T @ V_sq.T @ I_sq.T @ L_sq.T

print(transposed_product_sq)
print(live_evil_sq)
print(np.allclose(transposed_product_sq, live_evil_sq))