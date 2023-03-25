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

def isPrime(val):
    if val == 2:
        return True
    if val < 2 or val % 2 == 0:
        return False
    for i in range(3, int(val**0.5)+1, 2):
        if val % i == 0:
            return False
    return True

def delete_prime_CLL(a):
    curr = a.head
    while curr.next != a.head:
        if isPrime(curr.val):
            a.delete(curr.val)
        curr = curr.next


# Example usage
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

delete_prime_CLL(a)
a.print_list()
