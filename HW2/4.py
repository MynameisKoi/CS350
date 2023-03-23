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

# find common char values from 2 linked lists
# add the common char values to a new linked list
def commElem(l,m):
    l_set = set()
    m_set = set()
    curr_node = l.head
    curr_node2 = m.head
    res = LinkedList()
    while curr_node:
        l_set.add(curr_node.val)
        curr_node = curr_node.next
    while curr_node2:
        m_set.add(curr_node2.val)
        curr_node2 = curr_node2.next
    for i in l_set:
        if i in m_set:
            res.add_node(i)
    return res

# Example usage
a = LinkedList()
a.add_node("G")
a.add_node("O")
a.add_node("O")
a.add_node("D")
a.print_list()  # Head->G->O->O->D->NULL
b = LinkedList()
b.add_node("G")
b.add_node("o")
b.add_node("O")
b.add_node("g")
b.add_node("L")
b.add_node("E")
b.print_list()  # Head->G->o->O->g->L->E->NULL

c = commElem(a, b)
c.print_list()  # Head->G->O->NULL