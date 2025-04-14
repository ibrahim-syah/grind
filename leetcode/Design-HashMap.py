class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.arr = [ListNode(0,0) for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        selected = self.arr[key % len(self.arr)]
        while selected.next:
            if selected.next.key == key:
                selected.next.value = value
                return
            selected = selected.next
        selected.next = ListNode(key, value)
        
    def get(self, key: int) -> int:
        selected = self.arr[key % len(self.arr)]
        while selected.next:
            if selected.next.key == key:
                return selected.next.value
            selected = selected.next
        return -1
        
    def remove(self, key: int) -> None:
        selected = self.arr[key % len(self.arr)]
        while selected.next:
            if selected.next.key == key:
                selected.next = selected.next.next
                return
            selected = selected.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)