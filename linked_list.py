class SinglyNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)
D = SinglyNode(5)

head.next = A
A.next = B
B.next = C
C.next = D


def search(head, val):
    curr = head

    while curr:
        if val == curr.val:
            return True
        curr = curr.next

    return False

def display(head):
    curr = head
    elements = []

    while curr:
        elements.append(str(curr.val))
        curr = curr.next

    return " --> ".join(elements)

print(search(head, 3))
print(display(head))

class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

head = tail = DoublyNode(1)
print(head, tail)

def  insert_at_beginnig(val, head, tail):
    new_node = DoublyNode(val, head)
    head.prev = new_node

    return new_node, tail

head, tail = insert_at_beginnig(2, head, tail)
print(head, tail)

def  insert_at_end(val, head, tail):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node

    return head, new_node

head, tail = insert_at_end(3, head, tail)
print(head, tail)

def display_doubly(head):
    curr = head
    elements = []

    while curr:
        elements.append(str(curr.val))
        curr = curr.next

    return " <-> ".join(elements)
  
print(display_doubly(head))
