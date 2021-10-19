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

    def insert(self, value, after):  # insert after given index
        i = 1
        current = self.head
        while i < after and current is not None:
            current = current.next
            i += 1
        temp = Node(value)
        temp.next = current.next
        current.next = temp

    def pop(self):  # delete and output first element
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            return temp.value

    def remove_last(self):
        slast = self.head
        while slast.next.next:
            slast = slast.next
        temp = slast.next
        slast.next = None
        return temp.value

    def remove(self, after):
        current = self.head
        for _ in range(after):
            prev_node = current
            current = current.next
        temp = current
        prev_node.next = current.next
        current = None
        return temp.value

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
list_.insert(30, 2)
list_.listprint()
print("----------------")
print("usuniety: ", list_.remove(2))
list_.listprint()



