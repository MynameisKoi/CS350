class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def eval_tree(t: TreeNode) -> int:
    if not t:
        return 0

    if not t.left and not t.right:
        return t.val

    left_val = eval_tree(t.left)
    right_val = eval_tree(t.right)

    if t.val == '+':
        return left_val + right_val
    elif t.val == '-':
        return left_val - right_val
    elif t.val == '*':
        return left_val * right_val
    elif t.val == '/':
        return left_val / right_val
    elif t.val == '//':
        return left_val // right_val
    elif t.val == '%':
        return left_val % right_val
    elif t.val == '**':
        return left_val ** right_val
    else:
        raise ValueError(f"Invalid operator '{t.val}'")

if __name__ == '__main__':
    t = TreeNode('+')
    t.left = TreeNode(3)
    t.right = TreeNode('*')
    t.right.left = TreeNode('+')
    t.right.right = TreeNode(2)
    t.right.left.left = TreeNode(5)
    t.right.left.right = TreeNode(9)

    result = eval_tree(t)
    print(result) # 31