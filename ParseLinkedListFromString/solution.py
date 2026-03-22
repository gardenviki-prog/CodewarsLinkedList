from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None
    items = list_repr.split(" -> ")
    items.pop()
    result = None
    for i in reversed(items):
        result = Node(int(i), result)
    return result
