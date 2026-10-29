from collections import deque


class MyStack:
    def __init__(self):
        self.first = deque()
        self.second = deque()

    def push(self, x: int) -> None:
        self.second.append(x)
        while self.first:
            self.second.append(self.first.popleft())
        self.first, self.second = self.second, self.first

    def pop(self) -> int:
        return self.first.popleft()

    def top(self) -> int:
        return self.first[0]

    def empty(self) -> bool:
        return not self.first
