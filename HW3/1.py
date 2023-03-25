class Node:
    def __init__(self, value):
        self.value = value
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

    def traverse(self, skip):
        # this function will act as a wolf checking the nests
        current = self.head
        for i in range(skip):
            current = current.next
        print(f"Checking nest {current.value}")
        return current.value # return the nest that the wolf checked

    def is_nest_safe(self, n, size):
        current = self.head
        visited_nests = set()
        skip = 0
        for a in range(2, n):
            visit = self.traverse(skip)
            visited_nests.add(visit)
            current = current.next
            skip += a

        print(visited_nests)
        safe_nests = set(range(1, size)) - visited_nests
        if safe_nests:
            print(f"The following nests are safe: {sorted(safe_nests)}")
            return False
        else:
            print("All nests are unsafe.")
            return True

# Creating the linked list
ll = CircularLinkedList()
size = int(input("Enter the number of nests: "))
for i in range(size):
    ll.insert(i+1)

# input the number of times the wolf check the nest
n = int(input("Enter the number of times the wolf checks the nests: "))

# Determining safe nests after n checks
ll.is_nest_safe(n, size)  # Change the number of checks and skip value as needed
