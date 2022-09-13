import timeit
import numpy as np
import matplotlib.pyplot as plt

def foo(a):
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a


buble_sort = timeit.Timer("foo(a)", globals=globals())
plt_x = []
plt_sort = []

for i in range(100, 1001, 100):
    plt_x.append(i)

    a = np.random.randint(100, size=i)

    ps = buble_sort.timeit(number=50)
    plt_sort.append(ps)

    print("%15.5f" %(ps))

plt.plot(plt_x, plt_sort)
plt.show()