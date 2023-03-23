class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.val, end='->')
            curr_node = curr_node.next
        print('NULL')

def is_loopLL(a):

    if not a.head or not a.head.next:
        return False

    slow = a.head
    fast = a.head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

a = LinkedList()
a.add_node(1)
a.add_node(2)
a.add_node(3)
a.add_node(4)
a.add_node(5)
a.add_node(6)
a.print_list()  # Head->1->2->3->4->5->6->NULL
a.head.next.next.next.next = a.head.next.next # loop the linked list
print(is_loopLL(a))  # True

b = LinkedList()
b.add_node(1)
b.add_node(2)
b.add_node(3)
b.add_node(4)
b.add_node(5)
b.print_list()  # Head->1->2->3->4->5->NULL
print(is_loopLL(b))  # False