class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

a = Node(1)
b = Node(1)
c = Node(4)
d = Node(8)
e = Node(12)

f = Node(1)
g = Node(2)
h = Node(3)
i = Node(5)
j = Node(6)

head1 = a
a.next = b
b.next = c
c.next = d
d.next = e

head2 = f
f.next = g
g.next = h
h.next = i
i.next = j

def merge_lists(list1, list2):
    d = Node()
    curr = d

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            curr = list1
            list1 = list1.next
        else:
            curr.next = list2
            curr = list2
            list2 = list2.next

    curr.next = list1 if list1.next else list2

    return d.next

def show_list(head):
    list = head
    listing = ""

    while list:
        listing = listing + f" --> {list.val}"
        list = list.next

    return listing


merge_head = merge_lists(head1, head2)


print(show_list(merge_head))
print(show_list(head1))
print(show_list(head2))
