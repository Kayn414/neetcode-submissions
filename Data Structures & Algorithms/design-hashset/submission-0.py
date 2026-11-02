class MyHashSet:

    def __init__(self):
        self.list_obj = []

    def add(self, key: int) -> None:
        if key not in self.list_obj:
            self.list_obj.append(key)


    def remove(self, key: int) -> None:
        if key in self.list_obj:
            self.list_obj.remove(key)

        

    def contains(self, key: int) -> bool:
        return key in self.list_obj


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)