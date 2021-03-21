from Nodes import Node


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None


if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(7)
    s.push(8)
    s.push(10)
    s.pop()
    current = s.top
    while current:
        print(current.data)
        current = current.next