from unordered_list import UnorderedList

def move_to_front(list):
    line = input()

    if list.index(line) is not None:
        list.remove(line)

    list.add(line)


myList = UnorderedList()
n = int(input('Number of lines: '))
for i in range(n):
    move_to_front(myList)
    print(myList)