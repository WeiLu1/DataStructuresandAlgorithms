from Nodes import Node_DLL as Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, data):
        current = self.head
        node_deleted = False
        if current == None:
            node_deleted = False
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
        if node_deleted:
            self.count -= 1

    def iter(self):
        current = self.head
        while current:
            value = current.data
            current = current.next
            yield value

    def contains(self, data):
        for node_data in self.iter():
            if node_data == data:
                return True
            return False


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(5)
    dll.append(6)
    dll.append(7)
    dll.delete(5)

    current = dll.head
    while current:
        print(current.data)
        current = current.next
    containsbool = dll.contains(5)
    print(containsbool)
