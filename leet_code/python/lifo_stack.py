from collections import deque


class LifoStack:
    """
    A last-in-first-out (LIFO) stack using a Python's deque implementation.
    
    Example:
    myStack = LifoStack()
    myStack.push(1)
    myStack.push(2)
    myStack.pop()  # returns 2
    myStack.top()  # returns 1
    myStack.empty()  # returns False
    
    """

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.appendleft(x)

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0
