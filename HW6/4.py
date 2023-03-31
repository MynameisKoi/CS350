class CircularQueue:

    #Constructor
    def __init__(self, max):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = max

    #Adding elements to the queue
    def enqueue(self,data):
        if self.size() == self.maxSize-1:
            return ("Queue Full!")
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.maxSize
        return (f"{data} is enqueued.")

    #Removing elements from the queue
    def dequeue(self):
        if self.size()==0:
            return ("Queue Empty!")
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data

    #Calculating the size of the queue
    def size(self):
        if self.tail>=self.head:
            return (self.tail-self.head)
        return (self.maxSize - (self.head-self.tail))

    def isEmpty(self):
        return self.size() == 0

    def __str__(self):
        # print the queue from self.head to self.tail
        ans = ""
        for i in range(self.head, self.tail):
            ans += str(self.queue[i]) + " "
        return ans

    #Find out how many elements in the CircularQueue
    def getNumElem(self):
        ans = (self.tail - self.head) % self.maxSize
        return (f"The CircularQueue has {ans} element(s).")

q = CircularQueue(8)
print(q.enqueue(1))
print(q.enqueue(4))
print(q.enqueue(6))
print(q.enqueue(8))
print(q.enqueue(9))
print(q.enqueue(2))
print(q.enqueue(3))
print("Queue:",q)
print(q.getNumElem())
print(q.dequeue())
print(q.dequeue())
print("Queue:",q)
print(q.getNumElem())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print("Queue:",q)
print(q.getNumElem())