class MyQueue:

    def __init__(self):
        
        self.push_stack = []
        self.pop_stack = []
        
    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        
        if self.pop_stack == []:
            self.pop_stack = self.push_stack.copy()
            self.pop_stack = self.pop_stack[::-1]
            self.push_stack = []
        item = self.pop_stack.pop()
        return item

    def peek(self) -> int:
        if self.pop_stack != []:
            return self.pop_stack[-1]
        if self.push_stack != []:
            return self.push_stack[0]

    def empty(self) -> bool:
        return self.push_stack == [] and self.pop_stack == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()