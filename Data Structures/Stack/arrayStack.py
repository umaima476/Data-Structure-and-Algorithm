from array import array

class stack:
# the stack will be initialized with the user defined capacity as it is required by the constructor.
# there is nod need to maintain the "top" variable in python because of dynamic array and its built-in functions "append()" and "pop()"
    def __init__(self, capacity):
        self.stack = array('i')
        self.top = -1
        self.capacity = capacity

    def isEmpty(self):
        return len(self.stack) == 0
    
    def isFull(self):
        return self.stack == self.capacity
    
    def push(self, item):
        if self.isFull():
            return "The stack is full. No more elements can be added."
        else:
            self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return "The stack is empty. No element can be popped."
        else:
            self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "The stack is empty hence, topmost element is null."
        else:
            return self.stack[-1]
        
    def display(self):
        for i in range(len(self.stack)):
            print (self.stack[i])
        
s = stack(10)
s.push(7)
s.push(9)
s.push(11)
s.push(17)
s.push(19)
s.display()
s.pop()
s.display()
        