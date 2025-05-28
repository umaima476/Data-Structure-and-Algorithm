class stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            print("The stack is empty")
        else:
            self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print("The stack is empty")
        else:
            return self.stack[-1]

    def display(self):
        for i in range(len(self.stack)):
            print(self.stack[i])

s = stack()
s.push(5)
s.push(7)
s.push(11)
s.push(13)
s.display()
s.pop()
s.pop()
s.display()
print(f"The topmost element of the stack is {s.peek()}")