# Queues (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(13)
queue.append(12)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(234)
print(queue)

queue.pop() #pop right
print(queue)
