class Queue:
    def __init__(self, k):
        self.size = k
        self.queue = [0] * self.size
        self.front = -1
        self.rear = -1

    def isFull(self):
        if(self.front == 0 and self.rear == self.size-1):
            return True
        elif(self.front == self.rear + 1):
            return True
        else:
            return False
        
    def isEmpty(self):
        return self.front == -1

    def enqueue(self, element):
        if(self.isFull()):
            return "The Queue is full, no more elements can be added."
        else:
            if(self.front==-1):
                self.front = 0
            self.rear = (self.rear+1) % self.size
            self.queue[self.rear] = element

    def dequeue(self):
        if(self.isEmpty()):
            return "The Queue is empty nothing can be retrieved."
        elif(self.front == self.rear):
            ele = self.queue[self.front]
            self.front = self.rear = -1
            return ele
        else:
            ele = self.queue[self.front]
            self.front = (self.front+1) % self.size
            return ele
        
    def display(self):
        if(self.isEmpty()):
            return "The Queue is empty"
        elif(self.rear >= self.front):
            for i in range(self.front, self.rear+1):
                print(self.queue[i], end=" ") 
            print()
        else:
            for i in range(self.front, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear+1):
                print(self.queue[i], end=" ")
            print()

q = Queue(4)
q.enqueue(67)
q.enqueue(90)
q.enqueue(45)
q.enqueue(65)
q.display()
print("The element is removed:")
print(q.dequeue())
print("The queue after dequeue:")
q.display()