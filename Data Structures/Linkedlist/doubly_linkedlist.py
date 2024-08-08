class DoublyNode:
    def __init__(self, val, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self) -> str:
        return str(self.val)

    # Display the linked list
    def display(self):
        curr = self
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(' <-> '.join(elements))

    # Insert at the beginning - O(1)
    @staticmethod
    def insert_first(head, tail, val):
        new_node = DoublyNode(val, next=head)
        head.prev = new_node
        return new_node, tail

    # Insert at the end - O(1)
    @staticmethod
    def insert_last(head, tail, val):
        new_node = DoublyNode(val, prev=tail)
        tail.next = new_node
        return head, new_node

# Create the head and tail of the doubly linked list
head = tail = DoublyNode(1)
print(head, tail)

# Display the list
head.display()

# Insert at the beginning
head, tail = DoublyNode.insert_first(head, tail, 3)
head.display()

# Insert at the end
head, tail = DoublyNode.insert_last(head, tail, 43)
head.display()
