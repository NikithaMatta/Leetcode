class MyHashSet:

    def __init__(self):
        self.HashSet = set()

    def add(self, key: int) -> None:
        self.HashSet.add(key)

    def remove(self, key: int) -> None:
        if key in self.HashSet:
            self.HashSet.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.HashSet:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)