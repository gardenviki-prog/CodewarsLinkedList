class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None
    cur = head
    while cur.next:
        next_node = cur.next
        next_value = next_node.data
        if cur.data == next_value:
            cur.next = next_node.next
        else:
            cur = next_node
    return head
