""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    node = Node(data)
    if head is None or data < head.data:
        node.next = head
        head = node
    else:
        cur = head
        while cur.next is not None and cur.next.data < data:
            cur = cur.next
        node.next = cur.next
        cur.next = node
    return head
