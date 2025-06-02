'''

Теперь мы повторим ту же процедуру, но с другим сигналом и ядром. Цель 
будет состоять в том, чтобы сгладить неровный временной ряд. Временной 
ряд будет состоять из 100 случайных чисел, сгенерированных из гауссова рас-
пределения (также именуемого нормальным распределением). Ядро будет 
представлять собой функцию в  форме колокола, которая аппроксимирует 
гауссову функцию, определенную как числа [0, .1, .3, .8, 1, .8, .3, .1, 0],
но шкалированную так, чтобы сумма по ядру составляла 1.

'''


import numpy as np
import matplotlib.pyplot as plt

# Создаем случайный временной ряд из нормального распределения
def create_signal():
    np.random.seed(42)  # Для воспроизводимости результатов
    return np.random.randn(100)

# Создаем гауссово ядро
def create_gaussian_kernel():
    kernel = np.array([0, .1, .3, .8, 1, .8, .3, .1, 0])
    return kernel / kernel.sum()  # Нормализуем чтобы сумма была 1

# Функция для применения ядра к сигналу (свертка)
def apply_kernel(signal, kernel):
    kernel_size = len(kernel)
    result = np.zeros(len(signal))
    
    # Добавляем нули по краям для обработки границ
    padded_signal = np.pad(signal, (kernel_size//2, kernel_size//2), mode='constant')
    
    for i in range(len(signal)):
        segment = padded_signal[i:i+kernel_size]
        result[i] = np.dot(segment, kernel)
    
    return result

# Создаем сигнал и ядро
signal = create_signal()
time = np.arange(len(signal))
kernel = create_gaussian_kernel()

# Применяем ядро для сглаживания
smoothed_signal = apply_kernel(signal, kernel)

# Визуализация
plt.figure(figsize=(12, 8))

# График A: Ядро
plt.subplot(3, 1, 1)
plt.stem(np.arange(len(kernel)) - len(kernel)//2, kernel, 
        linefmt='b-', markerfmt='bo', basefmt=' ')
plt.title('A) Гауссово ядро для сглаживания')
plt.grid(True)

# График B: Исходный сигнал
plt.subplot(3, 1, 2)
plt.plot(time, signal)
plt.title('B) Исходный временной ряд (шумный)')
plt.grid(True)

# График C: Сглаженный сигнал
plt.subplot(3, 1, 3)
plt.plot(time, smoothed_signal)
plt.title('C) Сглаженный временной ряд')
plt.grid(True)

plt.tight_layout()
plt.show()