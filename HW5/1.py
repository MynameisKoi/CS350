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

# Function to sort the stack
def srt(stack):
    temp_stack = []

    while stack:
        # pop the top element from the input stack
        curr = stack.pop()

        # move all elements greater than current element from the temporary stack to the input stack
        while temp_stack and temp_stack[-1] < curr:
            stack.append(temp_stack.pop())
        # push the current element to the temporary stack
        temp_stack.append(curr)

    # copy the sorted elements from the temporary stack to the input stack
    while temp_stack:
        stack.append(temp_stack.pop())

# Driver program to test above functions
stack = createStack()
push(stack, "s")
push(stack, "o")
push(stack, "r")
push(stack, "t")

# TEST
print("Stack before sort: ", end="")
print(stack)
srt(stack)
print("Stack after sort: ", end="")
print(stack)