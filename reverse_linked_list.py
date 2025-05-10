class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

head = a
a.next = b
b.next = c
c.next = d
d.next = e

def reverse(head):
    curr = head
    prev = None

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    head = prev
    return head.val

print(reverse(head))
