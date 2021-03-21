from Nodes import Node_SLL as Node


class CircularlyLinkedList:     # Singly Ciruclar Linked list class
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.tail.next = self.head
        self.size += 1

    def delete(self, data):
        current = self.head
        prev = self.head
        while prev == current or prev != self.tail:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                self.size -= 1
            prev = current
            current = current.next


if __name__ == "__main__":
    cll = CircularlyLinkedList()
    cll.append(5)
    cll.append(6)
    cll.append(7)
    cll.append(8)
    cll.append(9)
    cll.append(0)

    cll.delete(5)

    current = cll.head
    counter = 0
    while current:
        print(current.data)
        current = current.next
        counter += 1
        if counter > 15:
            break