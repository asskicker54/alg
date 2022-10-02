from timeit import Timer
import numpy as np
import matplotlib.pyplot as plt
from sorts import quicksort, selection_sort, partition

fig = plt.figure()
ax = fig.add_subplot()

selection = Timer('selection_sort(x1)', globals=globals())
quick = Timer('quicksort(x2, 0, len(x2))', globals=globals())

plt_x = []
plt_s = []
plt_q = []

for _ in range(100, 1001, 100):
    plt_x.append(_)

    x1 = np.random.randint(-100, 100, [_])
    x2 = np.random.randint(-100, 100, [_])
    
    plt_s.append(selection.timeit(number=1))
    plt_q.append(quick.timeit(number=1))
    
ax.plot(plt_x, plt_s, label='Selection sort')
ax.plot(plt_x, plt_q, label='Quick sort')
ax.set_xlabel('Amount of elements')
ax.set_ylabel('Time')
ax.legend()
plt.savefig('./random.png')