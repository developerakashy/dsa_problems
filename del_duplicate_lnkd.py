class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

a = Node(1)
b = Node(1)
c = Node(2)
d = Node(3)
e = Node(3)

head = a
a.next = b
b.next = c
c.next = d
d.next = e

def deleteduplicates(head):
    curr = head

    while curr:
        while curr.next and curr.val == curr.next.val:
            curr.next = curr.next.next

        curr = curr.next

    return head

print(deleteduplicates(head))
