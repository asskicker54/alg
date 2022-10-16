from unordered_list import UnorderedList
import timeit
import matplotlib.pyplot as plt

class Stack:
    def __init__(self):
        self.list = UnorderedList()

    def __len__(self):
        return self.list.size()
    
    def push(self, item):
        self.list.add(item)
    
    def pop(self):
        return self.list.pop(0)

    def peek(self):
        return self.list.head.getData()
    
    def isEmpty(self):
        return self.list.size() == 0

class Queue:
    def __init__(self):
        self.list = UnorderedList()

    def __len__(self):
        return self.list.size()
    
    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        return self.list.pop(0)

    def isEmpty(self):
        return self.list.size() == 0
    

class Deque:
    def __init__(self):
        self.lst = UnorderedList()

    def __len__(self):
        return self.lst.size()
    
    def addFront(self, item):
        self.lst.add(item)
    
    def addRear(self, item):
        self.lst.append(item)
    
    def removeFront(self):
        return self.lst.pop(0)
    
    def removeRear(self):
        return self.lst.pop()
    
    def isEmpty(self):
        return self.lst.size() == 0

if __name__ == "__main__":
    stack = Stack()
    queue = Queue()
    deque = Deque()
    
    stack_time = timeit.Timer("stack.push(x)", globals=globals())
    queue_time = timeit.Timer("queue.enqueue(x)", globals=globals())
    deque_time = timeit.Timer("deque.addFront(x)", globals=globals())
    
    plt_x = []
    plt_s = []
    plt_q = []
    plt_d = []
    
    for i in range(1000, 10001, 1000):
        x = list(range(100))
        
        plt_x.append(i)
        plt_s.append(stack_time.timeit(number=100))
        plt_q.append(queue_time.timeit(number=100))
        plt_d.append(deque_time.timeit(number=100))

    plt.plot(plt_x, plt_s, label='stack')
    plt.plot(plt_x, plt_q, label='queue')
    plt.plot(plt_x, plt_d, label='deque')
    plt.xlabel('Elm')
    plt.ylabel('Time')
    plt.legend()
    plt.savefig('4.png')
