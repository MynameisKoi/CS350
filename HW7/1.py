class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class binaryTree:
    def __init__(self, root=None):
        self.root = root

    def printTree(self, root): #InOrder print
        if root:
            self.printTree(root.left)
            print(root.value, end=" ")
            self.printTree(root.right)

    def triple_leaves(self, root):
        if root is None:
            return

        # If the node is a leaf, triple its value
        root.value *= 3

        # Recursively triple the leaves in the left and right subtrees
        if (root.left): self.triple_leaves(root.left)
        if (root.right): self.triple_leaves(root.right)

# test
if __name__ == "__main__":
    # Create the tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Create the binary tree
    tree = binaryTree(root)

    # Print the tree
    print("Before:", end=" ")
    tree.printTree(root)
    print()

    # Triple the leaves
    tree.triple_leaves(root)

    # Print the tree
    print("After:", end= " ")
    tree.printTree(root)