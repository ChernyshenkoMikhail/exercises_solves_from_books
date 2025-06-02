'''

Замените 1 в центре ядра на –1 и усредните центр ядра. Затем выполните 
исходный код фильтрации и  построения графика повторно.

'''

import numpy as np
import matplotlib.pyplot as plt

def create_signal():
    np.random.seed(42)
    return np.random.randn(100)

def create_modified_kernel():
    kernel = np.array([0, .1, .3, .8, -1, .8, .3, .1, 0])
    kernel[3:6] = np.array([.8, -1, .8]).mean()
    return kernel / np.sum(np.abs(kernel))

def apply_kernel(signal, kernel):
    kernel_size = len(kernel)
    result = np.zeros(len(signal))

    padded_signal = np.pad(signal, (kernel_size//2, kernel_size//2), mode='constant')
    
    for i in range(len(signal)):
        segment = padded_signal[i:i+kernel_size]
        result[i] = np.dot(segment, kernel)
    
    return result

signal = create_signal()
time = np.arange(len(signal))

original_kernel = np.array([0, .1, .3, .8, 1, .8, .3, .1, 0])
original_kernel = original_kernel / original_kernel.sum()

modified_kernel = create_modified_kernel()

smoothed_original = apply_kernel(signal, original_kernel)
smoothed_modified = apply_kernel(signal, modified_kernel)

plt.figure(figsize=(12, 10))

plt.subplot(3, 1, 1)
plt.stem(np.arange(len(original_kernel)) - len(original_kernel)//2, 
        original_kernel, linefmt='b-', markerfmt='bo', basefmt=' ', label='Оригинальное')
plt.stem(np.arange(len(modified_kernel)) - len(modified_kernel)//2, 
        modified_kernel, linefmt='r-', markerfmt='ro', basefmt=' ', label='Модифицированное')
plt.title('A) Сравнение ядер: оригинального и модифицированного')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(time, signal)
plt.title('B) Исходный временной ряд (шумный)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(time, smoothed_original, 'b-', label='Оригинальное ядро')
plt.plot(time, smoothed_modified, 'r-', label='Модифицированное ядро')
plt.title('C) Сравнение сглаженных сигналов')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()