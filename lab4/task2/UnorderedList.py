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
        
    def __str__(self):
        res = ""
        current = self.head
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        while current != None:
            bolden = current is self.head
            res += f"{'[' + BOLD if bolden else ''}{current.getData()}{ENDC if bolden else ''}{']' if current.getNext() == None else ', '}"
            current = current.getNext()
        
        return res

    def __getitem__(self, slice):
        if isinstance(slice, int):
            current = self.head
            for _ in range(slice):
                current = current.getNext()
            return current.getData()
        
        s = slice.start if slice.start is not None else 0
        l = (slice.stop - s) if slice.stop is not None else (self.size() - s)
        # print(f"s: {s}, l: {l}")
        
        current = self.head
        temp = UnorderedList()
        
        for _ in range(s):
            current = current.getNext()
        for _ in range(l):
            temp.append(current.getData())
            current = current.getNext()
        
        return temp
            

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

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
    
    
    def print(self):
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        current = self.head
        
        while current != None:
            bolden = current is self.head
            print(f"{BOLD if bolden else ''}{current.getData()}{ENDC if bolden else ''}",
                  end=("" if current.getNext() == None else " -> "))
            current = current.getNext()
        print()
        
    
    def append(self, item):
        current = self.head
        
        if self.size() == 0:
            self.add(item)
        else:
            while current.getNext() != None:
                current = current.getNext()
            
            current.setNext(Node(item))
    
    def index(self, item):
        current = self.head
        count = 0
        while current != None:
            if current.getData() == item:
                return count
            else:
                count += 1
                current = current.getNext()
        if current == None:
            return None
        
    def insert(self, pos, item):
        current = self.head
        prev = None
        for _ in range(pos):
            prev = current
            current = current.getNext()
            
        temp = Node(item)
        temp.setNext(current)
        prev.setNext(temp)
    
    def pop(self, pos=None):
        current = self.head
        
        if pos is None:
            while current.getNext() != None:
                current = current.getNext()    
        else:
            for _ in range(pos):
                current = current.getNext()
                
        data = current.getData()
        self.remove(data)
        
        return data