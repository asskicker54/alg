#TODO: pop(pos, item)

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def append(self, item):
        current = self.head
        temp = Node(item)
        if self.size() == 0:
            self.add(item)
        else:
            while current.getNext() != None:
                current = current.getNext()
    
            current.setNext(temp)

    def insert(self, pos, item):
        current = self.head
        previous = None
        idx = 0
        temp = Node(item)

        while current != None and idx < pos:
            previous = current
            current = current.getNext()
            idx += 1

        if pos == 0:
            temp.setNext(self.head)
            self.head = temp
        else:
            if current == None:
                previous.setNext(temp)
            else:
                temp.setNext(current)
                previous.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def index(self, item):
        current = self.head
        idx = 0
        while current != None:
            if current.getData() != item:
                idx += 1
                current = current.getNext()
            else: 
                return idx
        if current == None:
            return None


    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def pop(self, pos=None):
        current = self.head

        if pos is None:
            while current.getNext() != None:
                current = current.getNext()
        else:
            for i in range(pos):
                current = current.getNext()

        data = current.getData()
        current.setData(None)

        return data

    def __str__(self):
        res = '['
        current = self.head
        while current != None:
            if res != '[':
                res += ' ' + str(current.getData())
            else:
                res += str(current.getData())
            current = current.getNext()
        res += ']'

        return res

