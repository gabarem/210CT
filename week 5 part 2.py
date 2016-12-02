def remove(self, n):
    if n.prev != None:
        n.prev.next = n.next
    else:
        self.head = n.next
    if n.next != None:
        n.next.prev = n.prev
    else:
        self.tail = n.prev
