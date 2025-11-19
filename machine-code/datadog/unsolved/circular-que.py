python


class MyCircularQueue:
    def __init__(self, k: int):
        """Initializes a fixed-size circular queue"""
        self.queue = [0] * k  # Initializes the array
        self.capacity = k       # Queue capacity
        self.size = 0           # Current number of elements in the queue
        self.head = 0           # Head pointer (points to the current head element)
        self.tail = 0           # Tail pointer (points to the next insertion position)

    def enQueue(self, value: int) -> bool:
        """Inserts an element to the rear of the queue"""
        if self.isFull():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity  # Handles the circular nature
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """Removes an element from the front of the queue"""
        if self.isEmpty():
            return False
        self.queue[self.head] = 0  # **Correction**: Logically clears the position (optional)
        self.head = (self.head + 1) % self.capacity  # Head pointer moves forward
        self.size -= 1
        return True

    def Front(self) -> int:
        """Gets the front element of the queue"""
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """Gets the rear element of the queue"""
        if self.isEmpty():
            return -1
        return self.queue[(self.tail - 1 + self.capacity) % self.capacity]  # **Correction**: Prevents incorrect calculation when `tail == 0`

    def isEmpty(self) -> bool:
        """Checks whether the queue is empty"""
        return self.size == 0

    def isFull(self) -> bool:
        """Checks whether the queue is full"""
        return self.size == self.capacity

    def size(self) -> int:
        """Gets the number of elements in the current queue"""
        return self.size

    def __str__(self):
        """Prints the queue state"""
        return f"Queue: {self.queue}, Head: {self.head}, Tail: {self.tail}, Size: {self.size}"


# Test code
queue = MyCircularQueue(5)
print(queue.enQueue(1))  # True
print(queue.enQueue(2))  # True
print(queue.enQueue(3))  # True
print(queue.enQueue(4))  # True
print(queue.enQueue(5))  # True
print(queue.enQueue(6))  # False (Queue is full)

print(queue.Front())  # 1
print(queue.Rear())   # 5
print(queue.deQueue())  # True
print(queue.enQueue(6))  # True (Circular insertion)
print(queue.Rear())   # 6
print(queue)  # View the internal state of the queue
