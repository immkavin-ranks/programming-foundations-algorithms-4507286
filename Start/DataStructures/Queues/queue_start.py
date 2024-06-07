# Example file for Programming Foundations: Algorithms by Joe Marini
# try out the Python queue functions
from collections import deque

# TODO: create a new empty deque object that will function as a queue

# list O(n)

queue = deque()

queue.append(1)
queue.append(3)
queue.append(4)
queue.append(15)

print(queue)
# TODO: add some items to the queue


# TODO: print the queue contents


# TODO: pop an item off the front of the queue
x = queue.popleft()

print(x)
print(queue)
y = queue.pop()
print(y)
print(queue)