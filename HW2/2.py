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

# add two linked list together
def add_LL(a, b):
    # extract the two integers from two linked lists
    a_int = 0
    b_int = 0
    curr_node = a.head
    while curr_node:
        a_int = a_int * 10 + curr_node.val
        curr_node = curr_node.next
    curr_node = b.head
    while curr_node:
        b_int = b_int * 10 + curr_node.val
        curr_node = curr_node.next
    # add the two integers
    c_int = a_int + b_int
    # convert the integer to a linked list
    c = LinkedList()
    while c_int:
        c.add_node(c_int % 10)
        c_int //= 10
    # reverse c to get the result
    curr_node = c.head
    prev_node = None
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    c.head = prev_node
    return c


# Example usage
a = LinkedList()
a.add_node(1)
a.add_node(2)
a.add_node(3)
a.add_node(4)
a.print_list()  # Head->1->2->3->4->NULL
b = LinkedList()
b.add_node(5)
b.add_node(6)
b.add_node(7)
b.add_node(8)
b.print_list()  # Head->5->6->7->8->NULL

c = add_LL(a, b)
c.print_list()  # Head->6->9->1->2->NULL