# linked list - collection of nodes
# Every node has: data and a pointer to the next node
class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    def get_next(self):
        return self.next_node
    def set_next(self, next_node):
        self.next_node = next_node
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data


class LinkedList(object):
    def __init__(self, root=None):
        self.root = root
        self.size = 0
    def get_size(self):
        return self.size
    # add data
    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1
    # remove data
    def remove(self, data):
        this_node = self.root
        prev_node = Node
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True # data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
        



