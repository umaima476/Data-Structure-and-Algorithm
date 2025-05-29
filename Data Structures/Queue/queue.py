class Queue:
    def __init__(self, k):
        self.size = k
        self.queue = [0] * k
        self.front = self.rear = -1

    def isEmpty(self):
        return self.front == -1
    
    def isFull(self):
        return self.rear == self.size - 1
    
    def enqueue(self, element):
        if (self.isFull()):
            return "The Queue is full. No more elements can be enqueue."
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear]=element
        else:
            self.rear += 1
            self.queue[self.rear] = element

    def dequeue(self):
        if(self.isEmpty()):
            return "The Queue is empty, nothing can be dequeue."
        
        elif (self.front >= self.rear):
            deEle = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return deEle
        
        else:
            deEle = self.queue[self.front]
            self.front += 1
            return deEle
        
    def display(self):
        if(self.isEmpty()):
            return " The Queue is empty, nothing can be displayed."
        else:
            for i in range(self.front, self.rear+1):
                print(self.queue[i])

q = Queue(6)
q.enqueue(55)
q.enqueue(66)
q.enqueue(88)
q.display()
print("The element deleted is:", q.dequeue())
q.display()