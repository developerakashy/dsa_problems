# O(2**n)  S(N)
def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

Head = SinglyNode(3)
A = SinglyNode(4)
B = SinglyNode(5)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

def display(Head):
    curr = Head
    elements = []

    while curr:
        elements.append(str(curr.val))
        curr = curr.next

    return " --> ".join(elements)

print(display(Head))

def reverse_display(node):
    if not node:
        return

    reverse_display(node.next)
    print(node)

reverse_display(Head)
