class Stack:
    def __init__(self):
        # class Stack but we will use one queue only to perform
        self.queue = []

    def push(self, val):
        self.queue.append(val)

    def pop(self):
        # the stack follows the Last-In-First-Out (LIFO) rule,
        # however, the queue follows the First-In-First-Out rule.
        # Therefore, we have to take out all elements in stack until
        # we reach the end of the stack and pop out
        n = len(self.queue)
        for _ in range(n-1):
            self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    # 5 - 4 - 3 - 2 - 1 (since Stack follow LIFO rule)
    print(stack.is_empty())
