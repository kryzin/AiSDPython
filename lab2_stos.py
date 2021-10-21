from typing import Any


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, element=Any):  # add a new element on top of stack
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def pop(self):  # output and delete first element
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            return temp.value

    def print(self):  # print out in a column
        temp = self.head
        while temp:
            print(temp.value, sep='\n')
            temp = temp.next

    def len(self):  # length of list
        if self.head is not None:
            current = self.head
            length = 1
            while current.next:
                length += 1
                current = current.next
            return length
        else:
            return 0

stos_ = Stack()
stos_.len()
stos_.push(13)
stos_.push(10)
stos_.push(5)
stos_.print()
print("rozmiar: ", stos_.len())

