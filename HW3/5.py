class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    def delete_node(self, node):
        if not node:
            print("Node to be deleted is not in the list")
            return
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end="->")
            current_node = current_node.next
        print("NULL")


def rotate_DLL(list, key):
    curr = list.head
    arr = []
    while curr is not None:
        arr.append(curr.data)
        curr = curr.next
    sub_arr1 = arr[:key][::-1]
    sub_arr2 = arr[key:][::-1]
    arr = sub_arr1 + sub_arr2
    ans = DoublyLinkedList()
    for i in arr:
        ans.insert(i)
    return ans

# test
a = DoublyLinkedList()
a.insert("a")
a.insert("b")
a.insert("c")
a.insert("d")
a.insert("e")
a.print_list()

b = rotate_DLL(a, 3)
print("Rotated: ", end="")
b.print_list()

c = DoublyLinkedList()
c.insert("c")
c.insert("i")
c.insert("v")
c.insert("i")
c.insert("c")
c.print_list()

d = rotate_DLL(c, 3)
print("Rotated: ", end="")
d.print_list()