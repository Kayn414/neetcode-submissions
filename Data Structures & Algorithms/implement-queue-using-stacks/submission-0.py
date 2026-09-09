class MyQueue:

    def __init__(self, max_size=100):
        self.queue = [None] * max_size
        self.front = 0
        self.rear = 0
        self.max_size = max_size
    
    def is_full(self):
        return self.rear == self.max_size 

    def push(self, x: int) -> None:
        if self.is_full():
            return
        self.queue[self.rear] = x
        self.rear += 1 

    def pop(self) -> int:
        if self.empty():
            return
        value = self.queue[self.front]
        self.front += 1 
        return value
        

    def peek(self) -> int:
        if self.empty():
            return None
        return self.queue[self.front]

    def empty(self) -> bool:
        return self.front == self.rear
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()