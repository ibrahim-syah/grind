class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.arr = [ListNode("dummy") for _ in range(1000)]

    def add(self, key: int) -> None:
        selected = self.arr[key % len(self.arr)]
        while selected.next:
            if selected.next.key == key:
                return
            selected = selected.next
        selected.next = ListNode(key)
        
    def remove(self, key: int) -> None:
        selected = self.arr[key % len(self.arr)]
        while selected.next:
            if selected.next.key == key:
                selected.next = selected.next.next
                return
            selected = selected.next

    def contains(self, key: int) -> bool:
        selected = self.arr[key % len(self.arr)]
        while selected.next:
            if selected.next.key == key:
                return True
            selected = selected.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)