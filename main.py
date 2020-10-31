import numpy as np
import matplotlib.pyplot as plt
import time


# Последовательное суммирование
def Posled(array):
    sum = 0
    for i in array:
        sum += i


def Piramid(array):
    y = array
    m = len(array)
    while m != 1:
        i = 0
        j = m - 1
        while i < j:
            y[i] = y[i] + y[j]
            i = i + 1
            j = j - 1
        m = int((m + 1) / 2)
    return y[0]


# if __name__ == "__main__":
#     print("Последовательное суммирование")
#     raz_1 = 0
#     mas_1 = []
#     time_1 = []
#     for i in range(0, 5):
#         raz_1 += 20000
#         array_1 = np.random.randint(0, 200, size=raz_1)
#         mas_1.append(raz_1)
#         start_time = time.time()
#         Posled(array_1)
#         time_1.append(float(time.time() - start_time))
#     # print(mas_1)
#     # print(time_1)
#     print("Пирамидальное суммирование")
#     raz_2 = 0
#     mas_2 = []
#     time_2 = []
#     for i in range(0, 5):
#         raz_2 += 20000
#         array_2 = np.random.randint(0, 200, size=raz_2)
#         mas_2.append(raz_2)
#         start_time = time.time()
#         Piramid(array_2)
#         time_2.append(float(time.time() - start_time))
#
#     fig, ax = plt.subplots()
#     ax.plot(mas_1, time_1, label='Послед')
#     # ax.plot(mas_2, time_2, label='Пирамид')
#     # ax.plot(mas_3, time_3, label='Пирамид')
#     # ax.plot(mas_4, time_4, label='Пирамид')
#     ax.legend()
#     fig.set_figheight(5)
#     fig.set_figwidth(8)
#     ax.set_title('Сравнение работ алгоритмов')
#     plt.show()

def segment(array):
    threadCount = 100
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    n = len(array)
    m = int(n / threadCount + 1)
    # start = 0
    # finish = 0
    k = 0
    while k < m:
        start = k * m
        if (k + 1) * m < n:
            finish = (k + 1) * m
        else:
            finish = n
        i = start
        while i < finish:
            y[k] += array[i]
            i = i + 1
        k = k + 1
    s = y[0]
    print(s)
    i = 0
    while i < threadCount:
        s = s + y[i]
    print(s)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    # print(Piramid(array))
    segment(array)
