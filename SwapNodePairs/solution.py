from preloaded import Node

def swap_pairs(head):
    if head is None:
        return None
    elif head.next is None:
        return head
    result = head.next
    prev = None
    while head is not None:
        if head.next is None:
            break
        else:
            second = head.next
            next_part = second.next
            second.next = head
            head.next = next_part
            if prev is not None:
                prev.next = second
            prev = head
            head = next_part
    return result
