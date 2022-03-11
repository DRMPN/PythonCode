# Implement Length() to count the number of nodes in a linked list.
# Implement Count() to count the occurrences of an integer in a linked list.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    n = 0
    while node:
        n += 1
        node = node.next
    return n

def count(node, data):
    c = 0
    while node:
        if node.data == data:
            c += 1
        node = node.next
    return c