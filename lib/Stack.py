
class Stack:

    def __init__(self, items = [], limit = 100):
        if items is None:
            items = []  
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.size() < self.limit:
            self.items.append(item)
        else:
            print("Stack is full.", item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() == self.limit

    def search(self, target):
        if target in self.items:
            return len(self.items) - 1 - self.items.index(target)
        
        return -1
