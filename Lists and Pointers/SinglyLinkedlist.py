from Nodes import Node_SLL as Node


class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append_On(self, data):
        node = Node(data)
        if self.tail is None:
            self.tail = node
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    def append_O1(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def iter(self):
        current = self.tail
        while current:
            value = current.data
            current = current.next
            yield value

    def delete(self, data):
        current = self.tail
        previous = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                self.size -= 1
            previous = current
            current = current.next

    def search(self, data):
        for node_value in self.iter():
            if data == node_value:
                return True
            return False

    def clear_list(self):
        self.head = None
        self.tail = None


def basic_list():
    n1 = Node('ham')
    n2 = Node('Spam')
    n3 = Node('Eggs')

    n1.next = n2
    n2.next = n3

    current = n1
    while current:
        print(current.data)
        current = current.next


def single_linked_list_On():
    s = SinglyLinkedList()
    s.append_On("hello")
    s.append_On("world")
    current = s.tail
    while current:
        print(current)
        current = current.next
    print(s.size)


def iterate_through():
    s = SinglyLinkedList()
    s.append_O1("hello")
    s.append_O1("world")
    s.append_O1("my")
    s.append_O1("name")
    s.append_O1("is")
    s.append_O1("wei")
    for word in s.iter():
        print(word)


if __name__ == "__main__":

    # basic_list()
    # single_linked_list_On()
    iterate_through()
