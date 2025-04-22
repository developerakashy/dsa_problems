from collections import deque

# Queue FIFO
q = deque()

q.append(1)
q.append(2)
q.append(3)

q.popleft()


print(q)

# stack LIFO
s = []

s.append(1)
s.append(2)
s.append(3)
s.append(4)

s.pop()

print(s)
