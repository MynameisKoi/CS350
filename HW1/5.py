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

def average_list(a):
    if not a.head:
        return 0
    curr_node = a.head
    sum = 0
    count = 0
    while curr_node:
        sum += curr_node.val
        count += 1
        curr_node = curr_node.next
    return sum/count


# Example usage
a = LinkedList()
a.add_node(1)
a.add_node(2)
a.add_node(3)
a.add_node(4)
a.print_list()  # Head->1->2->3->4->NULL
print("average_list(a): ", average_list(a))
