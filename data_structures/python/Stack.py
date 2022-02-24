
class Stack:
    def __init__(self):
        self.stack = []

    def top(self):
        return self.stack[-1] if self.stack else None

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def remove(self, item):
        self.stack.remove(item)


stack = Stack()
stack.push(2)
stack.push(1)
stack.remove(1)
print(stack.top())
