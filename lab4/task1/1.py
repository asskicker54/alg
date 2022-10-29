import lab4.task1.HashTable as HashTable

Ha = HashTable()

Ha[54] = "cat"
Ha[26] = "dog"
Ha[93] = "lion"
Ha[17] = "tiger"
Ha[77] = "bird"
Ha[31] = "cow"
Ha[44] = "goat"
print('Fill factor is 0.64 -> the next new element of the hash-table is going to increase the size of the hash-table')
Ha[55] = "pig"

print(Ha.culc_fill_factor())
del Ha['pig']
print(Ha.culc_fill_factor())
del Ha['goat']
print(Ha.culc_fill_factor())
del Ha['tiger']
print(Ha.culc_fill_factor())
print(Ha.data)
print(Ha.slots)
print(Ha.culc_fill_factor())
print(len(Ha), Ha.size)
print('Fill factor is lower then 0.2 -> reducing the size')
del Ha['cat']
print(Ha.data)
print(Ha.slots)
print(len(Ha), Ha.size)
'''
print(Ha.size)
print(Ha.data)
print(Ha.slots)
Ha[20] = "chicken"
print(Ha.slots)
print(Ha.data)

print(Ha[20])

print(Ha[17])
Ha[20] = 'duck'
print(Ha[20])
print(Ha[99])
print(len(Ha))
print('dcuck' in Ha)
print('duck' in Ha)
Ha[99] = 'chicken'
print(Ha.culc_fill_factor())
Ha[67] = 'asd'
print(Ha.culc_fill_factor())
Ha[33] = 'hfjsd'
print(Ha.culc_fill_factor())
Ha[11] = 'q'
print(Ha.culc_fill_factor())
Ha[12] = 'w'
print(Ha.culc_fill_factor())
Ha[5] = 'gf'
print(Ha.culc_fill_factor())
Ha[9] = 'bb'
print(Ha.culc_fill_factor())
print(Ha.data)
print(Ha.slots)
'''