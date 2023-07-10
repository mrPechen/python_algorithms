import queue

q = queue.Queue()

q.put(2)
q.put(3)
print(q.get()) #2
q.empty()
print(q.get()) #3
q.put(4)
q.put(5)
q.put(6)
print(q.get()) #4
q.empty()
print(q.get()) #5
q.empty()
print(q.get()) #6
