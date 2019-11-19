#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.count = 0
        print("self", self)
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) we alaways need to loop through all n nodes
        to count each item."""
        return self.count


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) if the LinkedList was empty when we start
        0(n) if LinkedList have items; we have to loop through the LinkedList
        until we get a node where it's next item is none
        """
        # counting the data
        self.count += 1
        # creating a new node
        new_node = Node(item)
        # check if the LinkedList is empty to make the new node the head
        if self.head is None:
            self.head = new_node
            self.tail =  new_node
            return
        # appending item to the tail
        self.tail.next = new_node
        self.tail = self.tail.next

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) we do not traverse through the
        LinkedList; we make the node the head node"""
        # counting the data
        self.count += 1
        # Creates new node to hold given item
        new_node = Node(item)
        # Point the new node to the head
        new_node.next = self.head
        self.head = new_node
        cur = self.head
        # Check if the only ele in the LinkedList is the head_node
        # and if it is set it to tail as well
        if cur.next is not None:
            return
        else:
            self.tail = new_node


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) if the item within the lambda function
        is the head no traversing is required.
        O(n)
        TODO: Worst case running time: O(n) traversing though the LinkedList is required
        in order to look for the item within the lambda function."""

        print("quality", quality)
        q  = quality
        cur = self.head
        # Loop through all nodes until we find item where quality(item) is True
        while cur is not None:
            if q(cur.data):
                return cur.data
            cur = cur.next


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) if the item to be removed is in the head_node no need to traverse.
        O(n) removing last element
        O(1) removing first element
        TODO: Worst case runn ing time: O(n) when traversing through the LinkedList is required"""
        # decreasing count by one when we are deleting an item
        self.count -= 1
        # if the only node is the head node
        cur = self.head
        if cur is not None and cur.data is item:
            # Check if the next element in the LinkedList is none
            if cur.next is None:
                self.tail = None
            self.head = cur.next # point the header to the next which is none
            cur = None  # delete the item by assigning it to none
            return item
        # traverse though LinkedList until we get none
        # or the node contains the item
        prev = None
        while cur is not None and cur.data is not item:
            prev = cur
            cur = cur.next
        # if we don't find the item then rasies error
        if cur is None:
            raise ValueError('Item not found: {}'.format(item))
            return item
        # if we find the item point the previous to the next next item
        # by jumping the cur item and set the cur to none
        prev.next = cur.next
        if cur.next is None:
            self.tail = prev
        cur = None

    def replace(self, item, sub):
        """add a new replace method to your LinkedList class that deletes an
           existing item and replaces it with a new item, without creating a new node."""
        self.delete(item)

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C', 'D', 1]:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))
    # print('delete: {}'.format(ll.delete("D")))
    print(ll.items())

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('head_node', ll.prepend("F"))
    # print('length: {}'.format(ll.length()))
    print('find: {}'.format(ll.find(lambda item: item == 'B')))
    # print(ll.items())
    print(ll.items())
    # print('delete: {}'.format(ll.delete("J")))
    print(ll.items())

    # Enable this after implementing delete methd
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
