'''

Ядро детектора резких изменений будет очень простым: [–1 +1].
Точечное произведение этого ядра на фрагмент сигнала временного ряда
с постоянным значением (например, [10 10]) равно 0.
Но это точечное произведение будет крупным, когда сигнал имеет
резкое изменение (например, [1 10] даст точечное произведение, равное 9).
Мы будем работать с сигналом, который будет представлен функцией плато.
Далее напишите цикл for для временных точек в сигнале. В каждый мо-
мент времени вычисляйте точечное произведение между ядром и сегментом 
данных временного ряда, который имеет ту же длину, что и ядро.
Смело продолжайте обследовать этот исходный код. Например, изменится 
ли что-нибудь, если дополнить ядро нулями ([0 –1 1 0])? А что, если пере-
вернуть ядро так, чтобы оно было [1 –1]? Как насчет того, если ядро будет 
асимметричным ([–1 2])?

'''

import numpy as np
import matplotlib.pyplot as plt

def create_signal():
    signal = np.zeros(100)
    signal[20:40] = 1
    signal[60:80] = -1
    return signal

def apply_kernel(signal, kernel):
    kernel_size = len(kernel)
    result = np.zeros(len(signal))
    
    for i in range(len(signal) - kernel_size + 1):
        segment = signal[i:i+kernel_size]
        result[i + kernel_size//2] = np.dot(segment, kernel)
    
    return result

signal = create_signal()
time = np.arange(len(signal))

kernel_basic = np.array([-1, 1])
detection_basic = apply_kernel(signal, kernel_basic)

kernel_padded = np.array([0, -1, 1, 0])
kernel_flipped = np.array([1, -1])
kernel_asymmetric = np.array([-1, 2])

detection_padded = apply_kernel(signal, kernel_padded)
detection_flipped = apply_kernel(signal, kernel_flipped)
detection_asymmetric = apply_kernel(signal, kernel_asymmetric)

plt.figure(figsize=(12, 10))

plt.subplot(3, 1, 1)
plt.stem([0, 1], kernel_basic, linefmt='b-', markerfmt='bo', basefmt=' ')
plt.title('A) Ядро детектора')
plt.ylim(-1.5, 1.5)
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(time, signal)
plt.title('B) Сигнал временного ряда')
plt.ylim(-1.5, 1.5)
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(time, detection_basic)
plt.title('C) Результат детектирования резких изменений')
plt.ylim(-1.5, 1.5)
plt.grid(True)

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(time, detection_padded)
plt.title('Ядро с дополненными нулями [0, -1, 1, 0]')
plt.ylim(-1.5, 1.5)
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(time, detection_flipped)
plt.title('Перевернутое ядро [1, -1]')
plt.ylim(-1.5, 1.5)
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(time, detection_asymmetric)
plt.title('Асимметричное ядро [-1, 2]')
plt.ylim(-1.5, 1.5)
plt.grid(True)

plt.tight_layout()
plt.show()