class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest): 
    first = source
    new_source = source.next
    first.next = dest
    return Context(new_source, first)
