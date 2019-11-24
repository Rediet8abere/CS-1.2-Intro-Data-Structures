class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList(object):

    def __init__(self):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node

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

    def append_after(self, data, after_data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node.next is None and cur_node.data == after_data:
            cur_node.next = new_node
            new_node.prev = cur_node
        else:
            before = None
            while cur_node.data != after_data:
                cur_node = cur_node.next
                before = cur_node.next
            new_node.prev = cur_node
            new_node.next = before
            cur_node.next = new_node
            before.prev = new_node

    def append_before(self, data, before_data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node.next is None and cur_node.data == before_data:
            self.head = new_node
            new_node.next = cur_node
            cur_node.prev = new_node

        else:
            after = None
            while cur_node.data != before_data:
                cur_node = cur_node.next
                after = cur_node.prev
            cur_node.prev = new_node
            new_node.next = cur_node
            new_node.prev = after
            after.next = new_node

    def items(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next

dll = DoublyLinkedList()

dll.prepend(0)

dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

dll.prepend(5)
dll.prepend(-1)

dll.append_after(6, 2)

dll.append_before(7, 3)

dll.items()
