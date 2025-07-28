class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if not self.queue:
            return []
        popped = self.queue[0]
        self.queue = self.queue[1:]
        return popped
    
    def size(self):
        return len(self.queue)
    
    def peak(self):
        if not len(self.queue):
            return []
        return self.queue[0]
        