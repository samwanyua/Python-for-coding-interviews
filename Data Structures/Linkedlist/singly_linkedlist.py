class SinglyNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return str(self.value)
    
    # Display the linked list
    def display(self):
        current = self
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print(' -> '.join(elements))

    # Search for a node value - O(n)
    def search(self, val):
        current = self
        while current:
            if val == current.value:
                return True
            current = current.next
        return False

# Create nodes and link them
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)
D = SinglyNode(10)

Head.next = A
A.next = B
B.next = C
C.next = D

# Display the list
Head.display()

# Search for a value
print(Head.search(10))
print(Head.search(5))
