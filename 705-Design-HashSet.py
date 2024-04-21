class MyHashSet:
    def __init__(self):
        self.mySet = set()        

    def add(self, key: int) -> None:
        self.mySet.add(key)

    def remove(self, key: int) -> None:
        if key in self.mySet:
            self.mySet.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.mySet