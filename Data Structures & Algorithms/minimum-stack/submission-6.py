class MinStack:
    def __init__(self):
        self.size = 0
        self.mins = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.size == 0:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1]))
        self.size += 1

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        self.size -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
