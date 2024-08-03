class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            print(f'Popped {item}')
        return 'Stack is empty!'

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return 'Stack is empty!'

    def size(self) -> int:
        return len(self.items)


stack = []

# Element qo'shish (push)
stack.append(10)
stack.append(20)
stack.append(30)

# Elementni olib tashlash (pop)
print(stack.pop())  # 30
print(stack.pop())  # 20
print(stack.pop())  # 10

# Deque
from collections import deque
queue = deque()

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.appendleft(item)

    def dequeue(self):
        if not self.is_empty():
            self.queue.popleft()
            return
        return 'Queue is empty ! '

    def peek(self):
        if not self.is_empty():
            return self.queue[-1]
        return 'Queue is empty ! '

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


# Element qo'shish (enqueue)
queue.append(10)
queue.append(20)
queue.append(30)

# Elementni olib tashlash (dequeue)
print(queue.popleft())  # 10
print(queue.popleft())  # 20
print(queue.popleft())  # 30
