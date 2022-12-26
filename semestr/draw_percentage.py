import numpy as np
import timeit
import matplotlib.pyplot as plt
from insertion_sort import insertion_sort
import random


def generate_percentage(n: int) -> np.ndarray:
    arr = np.random.randint(100, size=n)
    arr.sort()
    for i in range(int(n * 0.95), n):
        arr[i] = random.randint(0, 100)
    return arr


measure_time = timeit.Timer("insertion_sort(a)", globals=globals())
sizes = [100, 500, 1000, 2000, 4000, 6000, 8000, 10000]
plt_x = []
plt_sort = []

for i in sizes:
    plt_x.append(i)
    a = generate_percentage(n=i)

    ps = measure_time.timeit(number=50)
    plt_sort.append(ps)

plt.title("95% упорядочены, 5% рандомные")
plt.xlabel("Размер массива")
plt.ylabel("Время")
plt.plot(plt_x, plt_sort)
plt.savefig("./graphs/perc.png")
