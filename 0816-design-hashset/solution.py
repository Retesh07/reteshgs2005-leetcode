class MyHashSet:

    def __init__(self):
        self.hash = [False] * 1000001

    def add(self, key: int) -> None:
        self.hash[key] = True

    def remove(self, key: int) -> None:
        self.hash[key] = False

    def contains(self, key: int) -> bool:
        return self.hash[key]