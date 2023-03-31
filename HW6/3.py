from collections import deque

class priorityQueue:
    def __init__(self):
        self.queue = deque()
        self.size = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1
    def dequeue(self):
        if self.size == 0:
            return None
        else:
            # go through the queue one time to find the max element
            max = self.queue[0]
            for i in range(1, self.size):
                if self.queue[i] > max:
                    max = self.queue[i]
            # iterate through the queue to remove the max element
            self.size -= 1
            for i in range(self.size):
                if self.queue[i] == max:
                    self.queue[i] = self.queue[0]
                    self.queue[0] = max
                    break
            # remove the last element
            return self.queue.popleft()

    def isEmpty(self):
        return self.size == 0

    def __str__(self):
        return str(self.queue)

if __name__ == '__main__':
    queue = priorityQueue()
    queue.enqueue("C")
    queue.enqueue("O")
    queue.enqueue("D")
    queue.enqueue("A")
    print(queue)
    print(queue.dequeue())
    print(queue)
    queue.enqueue("B")
    print(queue)
    print(queue.dequeue())
    print(queue.isEmpty())
    print(queue)