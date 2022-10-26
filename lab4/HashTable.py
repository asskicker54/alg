class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.skip = 1
        self.fill_factor = None

    def culc_fill_factor(self):
        self.fill_factor = round(len(self) / self.size, 2)
        return self.fill_factor

    def increase_thesize(self):
        temp = [None] * self.size
        self.slots = self.slots + temp
        self.data = self.data + temp
        self.size = self.size * 2

    def reduce_thesize(self):
        self.size = self.size // 2

        slots_cpy = self.slots.copy()
        data_cpy = self.data.copy()
        temp = list(zip(slots_cpy, data_cpy))

        self.slots = [None] * self.size
        self.data = [None] * self.size

        for couple in temp:
            if couple[0] is not None:
                self.put(couple[0], couple[1])

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                        self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data
                      # replace
        if self.culc_fill_factor() > 0.7:
            self.increase_thesize()

    def hashfunction(self, key, size):
        return key % size

    def update_skip(self):
        if self.skip != self.size:
            self.skip += 1

    def rehash(self, oldhash, size):
        if self.skip == 1:
            return(oldhash + 1) % size
        else:
            self.update_skip()
            return (oldhash + self.skip**2) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __len__(self):
        count = 0
        for i in self.data:
            if i is not None:
                count += 1
        return count

    def __contains__(self, data):
        if data in self.data:
            return True
        else: 
            return False

    def __delitem__(self, item):
        try:
            idx = self.data.index(item)
            self.data[idx] = None
            self.slots[idx] = None
        except ValueError as e:
            print(f"Hash-Table has no item '{item}'")
        
        if self.culc_fill_factor() <= 0.2:
            self.reduce_thesize()