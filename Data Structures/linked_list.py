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
        current_node = self.root
        prev_node = None
        while current_node:
            if current_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(current_node.get_next())
                else:
                    self.root = current_node
                self.size -= 1
                return True # data removed
            else:
                prev_node = current_node
                current_node = current_node.get_next()
        return False # data not found
    
    # find 
    def find(self, data):
        current_node = self.root
        while current_node:
            if current_node.get_data() == data:
                return data
            else:
                current_node = current_node.get_next() 
        return None
    
    # print the entire linked list
    def print_list(self):
        current_node = self.root
        while current_node:
            print(current_node.get_data(), end=" -> ")
            current_node = current_node.get_next()

my_list = LinkedList()    
my_list.add(5)                                        
my_list.add(3)                                        
my_list.add(4)                                        
my_list.add(2)                                        
my_list.add(9)                                        
my_list.add(7)        
print(my_list.remove(5))   
print(my_list.find(94))                             
print(my_list.print_list())

    



        



