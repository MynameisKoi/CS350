class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

def rewrite_expression(expression):
    stack = Stack()
    new_expression = ""
    sign = Stack()
    var = Stack()

    # Iterate over each character in the expression
    for char in expression:
        if char == "(":
            if len(var.items) > 0:
                # this will be used where there are multiple parenthesis
                x = var.pop()
                y = sign.pop()
                var.push(x)
                var.push(x+y)
            else:
                # if there is no parenthesis ahead of this
                # push the new sign to stack 'var'
                var.push(sign.pop())
            stack.push(new_expression)
            new_expression = ""
        elif char == ")":
            if len(var.items) > 0:
                var.pop()
            old_expression = stack.pop()
            new_expression = old_expression + rewrite_expression(new_expression)
        elif char in "+-":
            sign.push(char)
            if len(var.items) > 0:
                a = var.pop()
                new_expression += a
                var.push(a)
            new_expression += char
        else:
            new_expression += char

    # Process the final expression in the stack
    while len(stack.items) > 0:
        old_expression = stack.pop()
        new_expression = old_expression + rewrite_expression(new_expression)

    # Rewrite the expression without parentheses
    result = new_expression.replace("+-", "-")
    result = new_expression.replace("-+", "-")
    result = result.replace("--", "+")

    return result

expression = "x - (y - z - (u + v)) - w"
new_expression = rewrite_expression(expression)
print(new_expression)  # "x - y + z + u + v - w"

expression = "x - (y + z)"
new_expression = rewrite_expression(expression)
print(new_expression)  # "x - y - z"