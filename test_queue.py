from linkedQ import LinkedQueue

q = LinkedQueue()

q.enqueue("A")
q.enqueue("b")
q.enqueue("5")

print(q)

print(q.peek())

print(q.dequeue())
print(q)