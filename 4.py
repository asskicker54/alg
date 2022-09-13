import timeit
import matplotlib.pyplot as plt
import random

del_array = timeit.Timer("del a[random.randrange(len(a))]", globals=globals())
del_dict = timeit.Timer("del d[random.randrange(len(d))]", globals=globals())

plt_x = []
plt_del_arr = []
plt_del_dict = []


for i in range(100, 1001, 100):
    plt_x.append(i)

    a = list(range(i))
    #pa = del_array.timeit(number=100)
    #plt_del_arr.append(pa)

    a = dict.fromkeys(range(i))
    pd = del_array.timeit()
    plt_del_dict.append(pd)
    


    print("%15.5f" %(pd))

#plt.plot(plt_x, plt_del_arr, plt_x, plt_del_dict)
#plt.show()