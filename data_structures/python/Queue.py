class Queue():
    def __init__(self):
        self.queue = []

    # adds item to the end of the queue
    def enqueue(self, data):
        self.queue.append(data)

    # removes item from front of the queue
    def dequeue(self, data):
        self.queue.pop(0)

    def front(self):
        print(self.queue[0])

    def rear(self):
        print(self.queue[-1])


queue = Queue()
queue.enqueue(1)

queue.front()
queue.rear()
