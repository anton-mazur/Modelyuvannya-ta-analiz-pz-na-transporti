class MyQueue:
    def __init__(self) -> None:
        self._in_stack: list[int] = []
        self._out_stack: list[int] = []

    def push(self, x: int) -> None:
        self._in_stack.append(x)

    def _move_to_out(self) -> None:
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())

    def pop(self) -> int:
        self._move_to_out()
        return self._out_stack.pop()

    def peek(self) -> int:
        self._move_to_out()
        return self._out_stack[-1]

    def empty(self) -> bool:
        return not self._in_stack and not self._out_stack


if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek(), queue.pop(), queue.empty())
