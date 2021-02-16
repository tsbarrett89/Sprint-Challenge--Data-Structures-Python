class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.contents = []
        self.oldest = 0

    def append(self, item):
        if len(self.contents) < self.capacity:
            self.contents.append(item)
        if self.oldest >= self.capacity:
            self.contents[0] = item
            self.oldest = 1
        else:
            self.contents[self.oldest] = item
            self.oldest += 1

    def get(self):
        return self.contents