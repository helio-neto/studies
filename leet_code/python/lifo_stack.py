class LifoStack:
    """A last-in-first-out (LIFO) stack using only one queue.
    
    # myStack object will be instantiated and called as such:
    # myStack = LifoStack()
    # myStack.push(x)
    # param_2 = myStack.pop()
    # param_3 = myStack.top()
    # param_4 = myStack.empty()
    
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
