# lista jednokierunkowa
from typing import Any


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value=Any):  # adds at the beginning
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value=Any):  # adds at the end
        new_node = Node(value)
        last_elem = self.head
        while last_elem.next:  # search for last element
            last_elem = last_elem.next
        last_elem.next = new_node

    def len(self):  # length of list
        current = self.head
        length = 0
        while current.next is not None:
            length += 1
            current = current.next
        return length

    def node(self, at: int):  # output value of input index
        if at > self.len() - 1:
            return "out of range"  # index is too big
        current_node = self.head
        for n in range(at):
            current_node = current_node.next
        return current_node.value

    def insert(self, value=Any, after=None):
        if after is None:
            return

        new_node = Node(value)
        prev_node = Node(after)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.value)
            printval = printval.next


list_ = LinkedList()
list_.head = Node(2)
e2 = Node(120)
e3 = Node(10)

list_.head.next = e2
e2.next = e3
list_.listprint()
print("----------------")
middle_node = list_.node(1)
list_.insert(value=30, after=middle_node)
# assert str(list_) == '2 -> 120 -> 30 -> 10'
list_.listprint()
