class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    def print_list(self):
        curr_node = self.head
        while curr_node.next != self.head:
            print(curr_node.val, end='->')
            curr_node = curr_node.next
        print(curr_node.val, end='->')
        print('NULL')
    def delete(self, key):
        if self.head is None: # if there is no CLL, return
            return
        if self.head.val == key and self.head.next == self.head: # if there is only one node in CLL, delete CLL
            self.head = None
            return
        last = self.head
        d = self.head
        while d.next != self.head:
            if d.val == key:
                break
            last = d
            d = d.next
        if d.val == key:
            if d == self.head:
                last = self.head
                while last.next != self.head:
                    last = last.next
                self.head = d.next
                last.next = self.head
            else:
                last.next = d.next
        else:
            print("Key not found")

def split_CLL(list, key):
    # split one CLL into two CLLs at the key position
    # return the two CLLs
    a = CircularLinkedList()
    b = CircularLinkedList()
    curr = list.head
    count = 0
    while curr.next != list.head:
        a.insert(curr.val)
        curr = curr.next
        count += 1
        if count == key:
            break
    while curr.next != list.head:
        b.insert(curr.val)
        curr = curr.next
    b.insert(curr.val)
    return a, b

a = CircularLinkedList()
a.insert(12)
a.insert(13)
a.insert(14)
a.insert(15)
a.insert(16)
a.insert(17)
a.insert(18)
a.insert(19)
a.insert(20)
a.print_list()

x, y = split_CLL(a, 3)
x.print_list()
y.print_list()
