class DoublyNode:
    def __init__(self, val, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self) -> str:
        return str(self.val)
    
head = tail = DoublyNode(1)
print(head, tail)

# display
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(elements))
display(head)

# insert at the beginning - O(1)
def insert_first(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail
head,tail = insert_first(head, tail, 3)
display(head)
