# singly linked list
class SinglyNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return str(self.val)
    
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)
D = SinglyNode(10)

Head.next = A
A.next = B
B.next = C
C.next = D