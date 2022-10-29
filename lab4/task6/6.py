import hashlib
import os
from HashTable import HashTable

path = input('Enter path -- ')
files = os.listdir(path)
print(files)

H = HashTable()

for f in files:
    url = path + f
    HASH = hashlib.sha256(open(url, 'rb').read()).hexdigest()
    if H[HASH] == None:
        H[HASH] = url
    else:
        print('Dublicates: ', H[HASH], url)
