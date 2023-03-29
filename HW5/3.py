from sys import maxsize

# Function to create a stack. It initializes size of stack as 0
def createStack():
    stack = []
    return stack

# Stack is empty when stack size is 0
def isEmpty(stack):
    return len(stack) == 0

# Function to add an item to stack. It increases size by 1
def push(stack, item):
    stack.append(item)

# Function to remove an item from stack. It decreases size by 1
def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1) # return minus infinite

    return stack.pop()

# Function to return the top from stack without removing it
def peek(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1) # return minus infinite
    return stack[len(stack) - 1]

def consecutive_seq(stack):
    var = []
    while (len(stack) != 0):
        var.append(stack.pop())

    ans = True
    while (len(var) > 1):
        x = var[-1]
        var.pop()
        y = var[-1]
        var.pop()
        if (abs(x-y) != 1):
            ans = False
        stack.append(x)
        stack.append(y)

    return ans

# Driver program to test above functions
stack = createStack()
push(stack, 4)
push(stack, 5)
push(stack, -2)
push(stack, -3)
push(stack, 11)
push(stack, 10)
push(stack, 5)
push(stack, 6)
push(stack, 20)

stack2 = createStack()
push(stack2, 4)
push(stack2, 6)
push(stack2, 6)
push(stack2, 7)
push(stack2, 4)
push(stack2, 3)

# test
print("Stack:", stack)
if (consecutive_seq(stack)):
    print("Yes")
    print("Consecutive sequence: ", end="")
    while (len(stack) != 0):
        print(stack.pop(), end=" ")
    print()
else:
    print("No")

print("Stack2:", stack2)
if (consecutive_seq(stack2)):
    print("Yes")
    print("Consecutive sequence: ", end="")
    while (len(stack2) != 0):
        print(stack2.pop(), end=" ")
    print()
else:
    print("No")