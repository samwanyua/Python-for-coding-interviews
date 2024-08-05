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
    def get


