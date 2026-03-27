def loop_size(node):
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    size = 0
    cur = slow
    while True:
        cur = cur.next
        size += 1
        if cur == slow:
            break
    return size
