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

def fib_tree(n):
    # n starts from 1, is the nth term of the series
    # base case
    if n == 0:
        return None
    elif n == 1:
        return Node(0)
    elif n == 2:
        return Node(1)
    elif n == 4: # special case where root.left = root.right
        root = Node(2)
        root.left = root.right = fib_tree(3)
        return root
    else:
        root = Node(fib_tree(n-1).value + fib_tree(n-2).value)
        root.left = fib_tree(n-2)
        root.right = fib_tree(n-1)
        return root

    # # create a Fib array for n values
    # fib = [0, 1]
    # for i in range(2, n+1):
    #     fib.append(fib[i-1] + fib[i-2])
    # # create a binary tree
    # root = Node(fib[n])
    # if n > 0:
    #     root.right = fib_tree(n-1)
    #     root.left = fib_tree(n-2) # root.right > root.left at all level
    # return root

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    # create a binary tree
    root = fib_tree(n)
    # create a binary tree object
    tree = binaryTree(root)
    # print the tree
    print("Inorder traversal: ", end="")
    tree.printTree(root)
