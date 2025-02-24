# List is not efficient for insert at beginning and removal from start

# Best to use deque from Collections

from collections import deque

queue = deque(['Alpha', 'Beta', 'Charlie'])

# Enqueue
queue.append('Delta')
print(queue)

# Deque
print(queue.popleft())