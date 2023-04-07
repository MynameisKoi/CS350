# create a linked list class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

def combine(ls):
    arr = []
    var = []
    # convert linkedList to list
    curr = ls.head
    while curr is not None:
        var.append(curr.data)
        curr = curr.next
    # combine the list
    for i in range(len(var)-1):
        alter_ls = var[:i] + [int(str(var[i])+str(var[i+1]))] + var[i+2:]
        arr.append(alter_ls)
    return arr

def transform(ls):
    arr = []
    for i in ls:
        n = []
        for x in i:
            if x > 26:
                n.append('#')
            else:
                n.append(chr(ord('A')+x-1))
        arr.append(n)
    return arr

# change from list to linkedList
def listToLinkedList(ls):
    ans = linkedList()
    for i in ls:
        ans.insert(i)
    return ans


# test program
ls = linkedList()
ls.insert(1)
ls.insert(2)
ls.insert(2)
ls.insert(1)
ls.display()
a = combine(ls) # [[12, 2, 1], [1, 22, 1], [1, 2, 21]]
# print(a)
b = transform(a) # [['L', 'B', 'A'], ['A', 'V', 'A'], ['A', 'B', 'U']]
# print(b)
for i in b:
    n = listToLinkedList(i)
    n.display()