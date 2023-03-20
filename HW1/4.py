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

def reverse_node(a):
    if not a.head:
        return

    prev_node = None
    curr_node = a.head
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    a.head = prev_node

# Example usage
a = LinkedList()
a.add_node(1)
a.add_node(2)
a.add_node(3)
a.add_node(4)
a.print_list()  # Head->1->2->3->4->NULL
reverse_node(a)
a.print_list()  # Head->4->3->2->1->NULL
