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
        while last_elem.next:
            last_elem = last_elem.next
        last_elem.next = new_node

    def len(self):  # length of list
        current = self.head
        length = 0
        while current.next is not None:
            length += 1
            current = current.next
        return length

    def node(self, at: int):  # output node of input index
        current = self.head
        i = 0
        while current:
            if i == at:
                return current
            i += 1
            current = current.next

    def insert(self, value, after):  # insert after given index
        if after is None:
            return
        new_node = Node(value)
        new_node.next = after.next
        after.next = new_node

    def pop(self):  # delete and output first element
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            return temp.value

    def remove_last(self):  # delete last node and output it
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        prev_last = self.head
        while (prev_last.next.next):
            prev_last = prev_last.next
        prev_last.next = None
        return prev_last

    def remove(self, after):  # delete node after given node
        prev = self.head
        curr = prev.next
        while prev is not None:
            if prev == after:
                prev.next = curr.next
                return curr
            prev = prev.next
            curr = curr.next

    def __str__(self):  # print out linked list
        cur = self.head
        out = ""
        while cur:
            out += str(cur.value) + " -> "
            cur = cur.next
        out = out.strip(" -> ")
        return out


list_ = LinkedList()
assert list_.head == None
list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'
list_.append(9)
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10'
middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'
first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element.value == returned_first_element
last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
#assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'
second_node = list_.node(at=1)
list_.remove(second_node)
assert str(list_) == '1 -> 5'

