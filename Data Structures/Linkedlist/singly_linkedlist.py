# singly linked list
class SinglyNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return str(self.value)
    

   


    
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)
D = SinglyNode(10)

Head.next = A
A.next = B
B.next = C
C.next = D

print(Head)

# Traverse the list - O(n)
current = Head
while current:
    print(current)
    current = current.next

# display
def display(head):
        current = head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print(' -> '.join(elements))

display(Head)

# search for a node value - O(1)
def search(head, val):
    curr = head
    while curr:
        if val == curr.value:
            return True
        curr = curr.next
    return False

print(search(Head,10))

