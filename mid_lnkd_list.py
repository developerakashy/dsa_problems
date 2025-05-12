class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

a = Node(1)
b = Node(1)
c = Node(4)
d = Node(8)
e = Node(12)

head = a
a.next = b
b.next = c
c.next = d
d.next = e

def middle(head):
    length = 0
    curr = head

    while curr:
        length += 1
        curr = curr.next

    mid = int(length/2) + 1

    new_curr = head
    count = 1
    while new_curr and count < mid:
        new_curr = new_curr.next
        count += 1

    return new_curr.val

print(middle(head))
