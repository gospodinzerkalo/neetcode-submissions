class MinStack:

    def __init__(self):
        self.minN = float('inf')
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if val <= self.minN:
            self.minN = val
            self.minStack.append(val)
        self.stack.append(val)


    def pop(self) -> None:
        if not self.stack: return
        if self.minStack and self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
            if self.minStack:
                self.minN = self.minStack[-1]
            else:
                self.minN = float('inf')
            
        self.stack.pop()
        

    def top(self) -> int:
        if not self.stack: return 0
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack: return 0
        return self.minN
