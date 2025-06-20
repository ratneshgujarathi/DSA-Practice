class Stack:
    def __init__(self, size=1000):
        self.size = size
        self.top = -1
        self.stack = [0] * size

    def push(self, x: int) -> None:
        self.top += 1
        self.stack[self.top] = x

    def pop(self) -> int:
        x = self.stack[self.top]
        self.top -= 1
        return x

    def peek(self) -> int:
        return self.stack[self.top]


    def size(self) -> int:
        return self.top + 1
    
    def is_empty(self) -> bool:
        return self.top == -1
    
    def print(self):
        stack = self.stack
        top = self.top
        if top == -1:
            print('stack is empty')
        while top != -1:
            print(stack[top])
            top-=1
    
    
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.print()