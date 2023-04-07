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

def pruning(t: binaryTree, k: int):
    # return a new tree that is a copy of only the first k levels of t
    # base case
    if k == 0:
        return None
    elif k == 1:
        return Node(t.root.value)
    else:
        root = Node(t.root.value)
        root.left = pruning(binaryTree(t.root.left), k-1)
        root.right = pruning(binaryTree(t.root.right), k-1)
        return root

# test
if __name__ == "__main__":
    # create a binary tree
    root = Node(5)
    root.left = Node(4)
    root.right = Node(3)
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.right.left = Node(2)
    root.right.right = Node(1)
    root.left.left.left = Node(2)
    root.left.left.left.left = Node(1)
    root.left.left.right = Node(1)
    root.left.right.left = Node(1)
    root.right.left.left = Node(1)
    # create a binary tree object
    tree = binaryTree(root)
    # print the tree
    print("Inorder traversal: ", end="")
    tree.printTree(root)
    print()
    # prune the tree
    k = int(input("Enter a number: "))
    newTree = pruning(tree, k) # prune a tree into k levels
    print("Inorder traversal: ", end="")
    tree.printTree(newTree)