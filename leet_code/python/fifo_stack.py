from collections import deque


class FifoStack:
    """
    A first-in-first-out (FIFO) queue using a Python's deque implementation.
    
    Example:
    stack = FifoStack()
    stack.push(1)
    stack.push(2)
    stack.pop()  # returns 1
    stack.peek()  # returns 2
    stack.empty()  # returns False

    """
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.popleft()

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
