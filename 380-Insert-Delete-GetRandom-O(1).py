import random


class RandomizedSet:
    def __init__(self):
        self.elements = []
        self.map = {}

    def insert(self, val):
        if val in self.map:
            return False

        self.elements.append(val)
        self.map[val] = len(self.elements) - 1
        return True

    def remove(self, val):
        if val not in self.map:
            return False

        idx = self.map[val]
        lastElement = self.elements[-1]

        self.elements[idx] = lastElement
        self.map[lastElement] = idx

        self.elements.pop()
        del self.map[val]
        return True

    def getRandom(self):
        return random.choice(self.elements)
