import timeit
import matplotlib.pyplot as plt
import random

inarr = timeit.Timer("random.randrange(len(a)) in a", globals=globals())
inset = timeit.Timer("random.randrange(len(s)) in s", globals=globals())

plt_x = []
plt_a = []
plt_s = []


for i in range(1_000_000, 10_000_001, 1_000_000):
    plt_x.append(i)

    a = list(range(i))
    pa = inarr.timeit(number=100)
    plt_a.append(pa)

    s = set(range(i))
    ps = inset.timeit(number=100)
    plt_s.append(ps)

    print("%15.5f, %15.5f" %(pa, ps))

plt.plot(plt_x, plt_a, plt_x, plt_s)
plt.savefig('./5.png')

