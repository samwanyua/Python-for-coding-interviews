class DoublyNode:
    def __init__(self, val, next, prev) -> None:
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self) -> str:
        return str(self.val)