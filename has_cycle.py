class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

a = Node(1)
b = Node(2)
c = Node(4)
d = Node(6)
e = Node(8)

head = a
a.next = b
b.next = c
c.next = d
d.next = e
# e.next = b

def has_cycle(head):
    d = Node()
    d.next = head
    slow = fast = d

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow is fast:
            return 1

    return -1

print(has_cycle(head))

