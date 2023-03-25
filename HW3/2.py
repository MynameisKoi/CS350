class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    def print_list(self):
        curr_node = self.head
        while curr_node.next != self.head:
            print(curr_node.val, end='->')
            curr_node = curr_node.next
        print(curr_node.val, end='->')
        print('NULL')

def commElem(l,m):
    l_set = set()
    m_set = set()
    curr_node = l.head
    curr_node2 = m.head
    res = CircularLinkedList()
    while curr_node.next != l.head:
        l_set.add(curr_node.val)
        curr_node = curr_node.next
    l_set.add(curr_node.val)
    while curr_node2.next != m.head:
        m_set.add(curr_node2.val)
        curr_node2 = curr_node2.next
    m_set.add(curr_node2.val)
    for i in l_set:
        if i in m_set:
            res.insert(i)
    return res

# Example usage
a = CircularLinkedList()
a.insert("G")
a.insert("O")
a.insert("O")
a.insert("D")
a.print_list()  # Head->G->O->O->D->NULL

b = CircularLinkedList()
b.insert("G")
b.insert("o")
b.insert("O")
b.insert("g")
b.insert("L")
b.insert("E")
b.print_list()  # Head->G->o->O->g->L->E->NULL

c = commElem(a,b)
c.print_list()