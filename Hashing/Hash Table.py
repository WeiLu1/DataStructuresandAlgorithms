class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def _hash(self, key):
        multiplier = 1
        hash_value = 0
        for ch in key:
            hash_value += multiplier * ord(ch)
            multiplier += 1
        return hash_value % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h] and self.slots[h].key == key:
                break
            h = (h + 1) % self.size
        if self.slots[h] is None:
            self.count += 1
            self.slots[h] = item

    def get(self, key):
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h + 1) % self.size


if __name__ == "__main__":
    ht = HashTable()

    # ht.put("one", "eggs")
    # ht.put("two", "ham")
    # ht.put("three", "bacon")
    # ht.put("four", "mushrooms")
    #
    # v = ht.get("two")
    # print(v)

    ht["one"] = "eggs"
    ht["two"] = "ham"
    print(ht["two"])

