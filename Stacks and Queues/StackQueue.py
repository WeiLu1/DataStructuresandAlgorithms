class StackQueue:
    def __init__(self):
        self.inbound_stack = []     # Store elements that are added to the queue
        self.outbound_stack = []    # elements can be deleted from our queue only through this stack

    def enqueue(self, data):
        self.inbound_stack.append(data)

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop()


if __name__ == "__main__":
    q = StackQueue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    print(q.inbound_stack)

    q.dequeue()
    print(q.inbound_stack)
    print(q.outbound_stack)
    q.dequeue()
    print(q.outbound_stack)
