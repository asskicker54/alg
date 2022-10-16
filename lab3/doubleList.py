class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def setData(self, newdata):
        self.data = newdata
        
    def setNext(self, newnext):
        self.next = newnext
        
    def setPrev(self, newprev):
        self.prev = newprev
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
            

class DoubleList():
    def __init__(self):
        self.head = None
    
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
    
    def __len__(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count
        
    def isEmpty(self):
        return self.head is None
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        
        if self.head is not None:
            self.head.prev = temp
        
        self.head = temp
            
    def append(self, item):
        temp = Node(item)
        current = self.head
        
        if self.head is None:
            temp.setPrev(None)
            self.head = temp
            return
        
        while current.getNext() is not None:
            current = current.getNext()
        
        current.setNext(temp)
        temp.setPrev(current)
    
    def removeFront(self):
        data = self.head.getData()
        self.head.getNext().setPrev(None)
        self.head = self.head.getNext()
        return data
    
    def removeRear(self):
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()
        
        data = current.getData()
        current.getPrev().setNext(None)
        return data
        
    def insertFront(self, pos, item):
        if pos >= len(self):
            print('out of range')
            return
        
        current = self.head
        prev = None

        for i in range(pos):
            prev = current
            current = current.getNext()
        
        temp = Node(item)
        prev.setNext(temp)
        temp.setPrev(prev)
        temp.setNext(current)
        current.setPrev(temp)        
    
    def insertRear(self, pos, item):
        if pos == len(self) - 1:
            self.append(item)
            return
        if pos < 0 or pos > len(self) - 1:
            print('out of range')
            return
        
        current = self.head
        for i in range(pos):
            current = current.getNext()
        
        temp = Node(item)
        temp.setNext(current.getNext())
        current.setNext(temp)
        temp.setPrev(current)
        
        if temp.getNext() is not None:
            temp.getNext().setPrev(temp)
            
    def remove(self, pos):
        if pos < 0 or pos >= len(self):
            print('out of range')
            return
        
        data = None
        if pos == 0:
            data = self.removeFront()
            return data
        if pos == len(self) - 1:
            data = self.removeRear()
            return data
        
        current = self.head
        for _ in range(pos):
            current = current.getNext()
        
        current.getPrev().setNext(current.getNext())
        current.getNext().setPrev(current.getPrev())
        data = current.getData()
        return data
        


if __name__ == "__main__":
    list = DoubleList()

    list.add(1)
    list.append(2)
    list.append(3)

    list.insertFront(1, 2.5)
    list.insertRear(3, 3.5)
    print(list)
    print(list.removeRear())
    print(list)
    print(list.removeFront())
    print(list)
    print(list.search(3))
    print(list.remove(1))
    print(list)
    print(list.remove(2))
    print(list)