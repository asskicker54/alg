import timeit
import matplotlib.pyplot as plt
import numpy as np

#первый алгоритм; сложность = O(n)
def find_Max_Min_first(a):
    maxi = 0
    mini = 100
    for i in range(len(a)):
        if a[i] > maxi:
            maxi = a[i]
        if a[i] < mini:
            mini = a[i]
        
    return maxi, mini

def find_Max_Min_second(a):
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a[0], a[len(a)-1]

first = timeit.Timer("find_Max_Min_first(a)", globals=globals())
second = timeit.Timer("find_Max_Min_second(a)", globals=globals())

plt_x = []
plt_first = []
plt_second = []

for i in range(100, 1001, 100):
    plt_x.append(i)

    a = np.random.randint(100, size=i)
    pf = first.timeit(number=50)
    plt_first.append(pf)

    a = np.random.randint(100, size=i)
    ps = second.timeit(number=50)
    plt_second.append(ps)

    print("%15.5f, %15.5f" %(pf, ps))

plt.plot(plt_x, plt_first, plt_x, plt_second)
plt.savefig('./2.png')

