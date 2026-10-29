class MinStack:
    def __init__(self) -> None:
        self._values: list[int] = []
        self._minimums: list[int] = []

    def push(self, val: int) -> None:
        self._values.append(val)
        if not self._minimums or val <= self._minimums[-1]:
            self._minimums.append(val)

    def pop(self) -> None:
        value = self._values.pop()
        if value == self._minimums[-1]:
            self._minimums.pop()

    def top(self) -> int:
        return self._values[-1]

    def getMin(self) -> int:
        return self._minimums[-1]


if __name__ == "__main__":
    stack = MinStack()
    for value in (-2, 0, -3):
        stack.push(value)
    print(stack.getMin())
    stack.pop()
    print(stack.top(), stack.getMin())
