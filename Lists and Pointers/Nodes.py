class Node_SLL:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Node_DLL:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


if __name__ == "__main__":
    n = Node_SLL(5)
    print(n)
