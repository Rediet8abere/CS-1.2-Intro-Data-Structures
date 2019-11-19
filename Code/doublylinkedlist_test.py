from doublylinkedlist import DoublyLinkedList, Node
import unittest

class NodeTest(unittest.TestCase):

    def test_init(self):
        data = 'ABC'
        node = Node(data)
        # Initialize should add data
        assert node.data is data
        assert node.next is None
        assert node.prev is None

    def test_linked_list(self):
        node_one = Node('A')
        node_two = Node('B')
        node_three = Node('C')
        # link nodes to the next nodes
        node_one.next = node_two
        node_two.next = node_three
        node_three.next = None
        # link nodes to previous nodes
        node_one.prev = None
        node_two.prev = node_one
        node_three.prev = node_two

        # nodes link should be transitive
        assert node_one.next is node_two
        assert node_two.next is node_three
        assert node_three.next is None

        assert node_one.prev is None
        assert node_two.prev is node_one
        assert node_three.prev is node_two


class DoublyLinkedList(unittest.TestCase):

    def test_init(self):
        dll = DoublyLinkedList()
        assert dll.head is None  # First node
        assert dll.tail is None  # Last node
