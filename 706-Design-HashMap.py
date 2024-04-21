class MyHashMap:
    def __init__(self):
        self.hashMap = {}

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.hashMap[key] = value
        else:
            self.hashMap[key] = value

    def get(self, key: int) -> int:
        if key in self.hashMap:
            return self.hashMap[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.hashMap:
            del self.hashMap[key]
