class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doublylinkedlist(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = cur_node
            new_node.next = None
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            cur_node = self.head
            self.head = new_node
            self.head.next = cur_node
            self.head.prev = None
            cur_node.prev = self.head

    def items(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next

dll = Doublylinkedlist()

dll.prepend(0)

dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

dll.prepend(5)
dll.prepend(-1)

dll.items()
