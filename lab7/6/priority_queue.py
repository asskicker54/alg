from binheap import BinHeap


class PQItem:
    def __init__(self, data: any, priority: int) -> None:
        self.data = data
        self.priority = priority

    def __repr__(self) -> str:
        return str(self.data)

    def __gt__(self, other) -> bool:
        return True if self.priority > other.priority else False

    def __lt__(self, other) -> bool:
        return True if self.priority < other.priority else False


class PriorityQueue:
    def __init__(self) -> None:
        self.heap = BinHeap()

    def enqueue(self, item: any, priority: int) -> None:
        self.heap.insert(PQItem(item, priority))

    def dequeue(self):
        return self.heap.delMin().data


pq = PriorityQueue()
pq.enqueue(1, 1)
pq.enqueue(2, 2)
pq.enqueue("3", 3)
pq.enqueue("10", 1)

print(pq.heap.heapList)
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
