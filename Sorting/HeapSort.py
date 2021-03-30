class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def float_min(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k // 2]:
                temp = self.heap[k]
                self.heap[k] = self.heap[k // 2]
                self.heap[k // 2] = temp
            k //= 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.float_min(self.size)

    def min_index(self, k):
        if (k * 2) + 1 > self.size:
            return k * 2
        elif self.heap[k * 2] < self.heap[(k * 2) + 1]:
            return k * 2
        else:
            return k * 2 + 1

    def sink(self, k):
        while k * 2 <= self.size:
            mi = self.min_index(k)
            if self.heap[k] > self.heap[mi]:
                temp = self.heap[k]
                self.heap[k] = self.heap[mi]
                self.heap[mi] = temp
            k = mi

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item

    def heap_sort(self):
        sorted_list = []
        for node in range(self.size):
            n = self.pop()
            sorted_list.append(n)
        return sorted_list
