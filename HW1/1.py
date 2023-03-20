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

def Delete_LinkList_Node(a, key):
        while a.head and a.head.val == key:
            a.head = a.head.next

        curr_node = a.head
        while curr_node and curr_node.next:
            if curr_node.next.val == key:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next


# Example usage
a = LinkedList()
a.add_node(1)
a.add_node(2)
a.add_node(1)
a.add_node(3)
a.print_list()  # Head->1->2->1->3->NULL
Delete_LinkList_Node(a,1)
a.print_list()  # Head->2->3->NULL
