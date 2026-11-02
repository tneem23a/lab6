class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.last is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def dequeue(self):
        if self.first is None:
            return None

        value = self.first.value
        self.first = self.first.next

        if self.first is None:
            self.last = None

        return value

    def isEmpty(self):
        return self.first is None

    def peek(self):
        if self.first is None:
            return None
        return self.first.value

    def __str__(self):
        result = ""
        current = self.first

        while current:
            result += current.value
            current = current.next

        return result