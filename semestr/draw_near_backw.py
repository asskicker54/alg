import numpy as np
import timeit
import matplotlib.pyplot as plt
from insertion_sort import insertion_sort


def generate_near_backw_array(n: int) -> np.ndarray:
    arr = np.random.randint(100, size=n)
    arr.sort()
    arr[n // 2], arr[n // 2 + 1] = arr[n // 2 + 1], arr[n // 2]
    return arr[::-1]


measure_time = timeit.Timer("insertion_sort(a)", globals=globals())
sizes = [100, 500, 1000, 2000, 4000, 6000, 8000, 10000]
plt_x = []
plt_sort = []

for i in sizes:
    plt_x.append(i)
    a = generate_near_backw_array(n=i)
    print(a)
    ps = measure_time.timeit(number=50)
    plt_sort.append(ps)

plt.title("Почти отсортированный в обратную сторону")
plt.xlabel("Размер массива")
plt.ylabel("Время")
plt.plot(plt_x, plt_sort)
plt.savefig("./graphs/backw.png")
