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
    print(item + " pushed to stack ")

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

def next_bigger(stck):
    stack = []
    result = {}

    # iterate through each element in the stack
    for val in stck:
        # if the stack is not empty and the current element is greater than the top element of the stack
        while len(stack) != 0 and int(val) > int(stack[-1]):
            # pop the top element of the stack and set its next bigger value as the current element
            print(stack.pop(),"->",val, end=", ")
        # push the current element to the stack
        stack.append(val)
    # set the next bigger value as None for any remaining elements in the stack
    while len(stack) > 1:
        print(stack.pop(),"->",None, end=", ")
    print(stack.pop(),"->",None, end="")

# Driver program to test above functions
stack = createStack()
push(stack, str(5))
push(stack, str(3))
push(stack, str(2))
push(stack, str(10))
push(stack, str(6))
push(stack, str(8))
push(stack, str(1))
push(stack, str(4))
push(stack, str(12))
push(stack, str(7))
push(stack, str(4))
print("Stack:", stack)

# test
next_bigger(stack)