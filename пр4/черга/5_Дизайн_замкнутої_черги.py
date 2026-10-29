class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [0] * k
        self.capacity = k
        self.front_index = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        rear = (self.front_index + self.size) % self.capacity
        self.data[rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front_index = (self.front_index + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.front_index]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.front_index + self.size - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
