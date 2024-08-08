class DoublyNode:
    def __init__(self, val, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self) -> str:
        return str(self.val)
    
head = tail = DoublyNode(1)
print(head, tail)