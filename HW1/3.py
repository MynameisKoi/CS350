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

def delete_dup_node(a):
        if not a.head:
            return

        val_set = set()
        curr_node = a.head
        prev_node = None

        while curr_node:
            if curr_node.val in val_set:
                prev_node.next = curr_node.next
            else:
                val_set.add(curr_node.val)
                prev_node = curr_node
            curr_node = curr_node.next

# Example usage
a = LinkedList()
a.add_node(1)
a.add_node(2)
a.add_node(1)
a.add_node(3)
a.add_node(2)
a.print_list()  # Head->1->2->1->3->2->NULL
delete_dup_node(a)
a.print_list()  # Head->3->NULL
