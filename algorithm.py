# Linear search

# def linear_search(array: list, target: int) -> int:
#     for item in array:
#         if item == target:
#             return array.index(target)
#         else:
#             return None
#
#
# arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(linear_search(arr, 30))

# def linear_search(arr: list, target: int) -> int:
#     for index in range(len(arr)):
#         if arr[index] == target:
#             return index
#         else:
#             return None
#
#
# arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(linear_search(arr, 30))


# Binary Search
#
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 6
# print(binary_search(arr, target))

# my_list = ['c', 'c++', 'java', 'python', 'ruby']
# my_list.sort()
# print(my_list)
# print(binary_search(my_list, 'c++'))

# result = binary_search(arr, target)
# if result != -1:
#     print(f'element is indexes {result}')
# else:
#     print(f'element is {target} not found')


# stack = lifo
# queue = fifo


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
            print(f'Popped item {item}')

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self) -> int:
        return len(self.items)


# Stack = is_empty,push,pop,peek,size


# def search(arr, target):
#     for item in arr:
#         if item == target:
#             return arr.index(target)
#
#
# def search1(arr, target):
#     for index in range(len(arr)):
#         if arr[index] == target:
#             return index


# def main(arr, target):
#     low, high = 0, len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1


from collections import deque


# class Queue:
#     def __init__(self):
#         self.queue = deque
#
#     def is_empty(self) -> bool:
#         return len(self.queue) == 0
#
#     def enqueue(self, item) -> None:
#         self.queue.appendleft(item)
#
#     def dequeue(self):
#         if not self.is_empty():
#             self.queue.popleft()
#             return
#         return 'Queue is empty'
#
#     def peek(self):
#         if not self.is_empty():
#             return self.queue[-1]
#
#     def size(self) -> int:
#         return len(self.queue)


# class Custom_Queue:
#     def __init__(self):
#         self.queue = []
#
#     def is_empty(self) -> bool:
#         return len(self.queue) == 0
#
#     def enqueue(self, item) -> None:
#         self.queue[0].push(item)
#
#     def dequeue(self):
#         if not self.is_empty():
#             self.queue.pop(0)
#             return
#         return 'Queue is empty'
#
#     def peek(self):
#         if not self.is_empty():
#             return self.queue[-1]
#
#     def size(self) -> int:
#         return len(self.queue)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def add_first(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def after_node_add(self, prev_node, new_data):
        if not prev_node:
            print('No previous node')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None


nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeA.next = nodeB
nodeB.next = nodeC
