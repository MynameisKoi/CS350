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

# sort given linked list with char type node
def srt_LL(ls):
    # find the length of the linked list
    len = 0
    curr_node = ls.head
    while curr_node:
        len += 1
        curr_node = curr_node.next
    # sort the linked list
    for i in range(len):
        curr_node = ls.head
        for j in range(len - 1):
            if curr_node.val > curr_node.next.val:
                temp = curr_node.val
                curr_node.val = curr_node.next.val
                curr_node.next.val = temp
            curr_node = curr_node.next


# Example usage
a = LinkedList()
a.add_node("D")
a.add_node("A")
a.add_node("C")
a.add_node("A")
a.add_node("G")
a.print_list()  # Head->1->2->1->3->NULL
srt_LL(a)
a.print_list()  # Head->2->3->NULL
