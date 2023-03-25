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
        # in order to check the prev pointer
        # we need to print out the linked list in both ways
        current_node = self.head
        print("Forward: ", end="")
        while current_node is not None:
            print(current_node.data, end="->")
            current_node = current_node.next
        print("NULL")
        # print backward pointer
        # for each Node in DLL, print where the prev pointer points at
        current_node = self.tail
        print("Backward pointer: ")
        while current_node is not None:
            print(current_node.data, end="->")
            current_node = current_node.prev
        print("NULL")

def correctPointer(a):
    if a.head == None:
        return
    temp = a.head
    # check the pointer at the head first
    if (a.head.next != None and a.head.next.prev != a.head):
        a.head.next.prev = a.head
    if a.head.prev != None:
        a.head.prev = None # if DLL, head.prev must be None
    # check the rest of the list
    temp = temp.next
    # if the temp.next's previous pointer is incorrect, correct it
    while (temp.next != None):
        if (temp.next.prev != temp):
            temp.next.prev = temp
        # if the temp.prev's next pointer is incorrect, correct it
        if (temp.prev.next != temp):
            temp.prev.next = temp
        temp = temp.next
    return a

# test
a = DoublyLinkedList()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
# create an incorrect pointer
a.head.next.next.next.prev = a.head.next
a.head.next.next.next.next.prev = a.head.next.next
print("Incorrect Linked List: ")
a.print_list()
b = correctPointer(a)
print("Corrected Linked List: ")
b.print_list()
