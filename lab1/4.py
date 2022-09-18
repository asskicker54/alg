import timeit
import matplotlib.pyplot as plt

def create_dict(n):
    key = [f"{i}" for i in range(n)]
    value = [i for i in range(n)]

    return dict(zip(key, value))

del_array = timeit.Timer("del a[i//2]", globals=globals())
del_dict = timeit.Timer("del d[f'{i//2}']", globals=globals())

plt_x = []
plt_del_arr = []
plt_del_dict = []


for i in range(1_000_000, 10_000_001, 1_000_000):
    plt_x.append(i)

    a = list(range(i))
    d = create_dict(i)

    pa = del_array.timeit(number=100)
    plt_del_arr.append(pa)

    pd = del_array.timeit(number=100)
    plt_del_dict.append(pd)
    
    print("%15.5f, %15.5f" %(pa, pd))

plt.plot(plt_x, plt_del_arr, plt_x, plt_del_dict)
plt.savefig('./4.png')