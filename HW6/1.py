from collections import deque

def genBin(n):
    # Create a queue to store binary numbers
    queue = deque()

    # Enqueue the first binary number
    queue.append('1')

    # Loop until n is reached
    while int(queue[0], 2) <= n:
        # Dequeue the next binary number
        binary_number = queue.popleft()
        # Print the binary number
        print(binary_number)

        # Enqueue the next binary number by adding a '0' and '1' to the current binary number
        queue.append(binary_number + '0')
        queue.append(binary_number + '1')

# Driver code
if __name__ == '__main__':
    n = 10
    genBin(n)
    