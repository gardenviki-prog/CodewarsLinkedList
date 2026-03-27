class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    first_list = head
    second_list = head.next
    ptr1 = first_list
    ptr2 = second_list
    current = head.next.next
    while current:
        ptr1.next = current
        ptr1 = ptr1.next
        if current.next:
            ptr2.next = current.next
            ptr2 = ptr2.next
            current = current.next.next
        else:
            break
    ptr1.next = None
    ptr2.next = None
    return Context(first_list, second_list)
