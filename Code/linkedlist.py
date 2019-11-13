#!python
# when we create an array object in memory it is contigious
#  ll is not contigious

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
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        cur = self.head
        length = 0
        while cur is not None:
            cur = cur.next
            length += 1
        return length


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        # once we know where we are  in the list it just involves shifting the next and previous pointers around; it is
        #  a constant time operation
        # In an array in the worst case if we need to insert an item in the begining of the array, it will involve
        # all of the elements to the right inorder to make a room for the item we want to insert.
        # TODO: Create new node to  hold given item
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail =  new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
            self.tail =  last_node
        last_node.next = new_node
        self.tail = new_node

        # TODO: Append node after tail, if it exists

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        cur = self.head
        if cur.next is not None:
            return
        else:
            self.tail = new_node


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        O(n)
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

        #  Arrays are constant time operation  if we give it the index it can immedialty give us the ele at
        # which the entry is stored because arrays are contigious
        # Accessing element in ll is in order of n operations. If we need to access an element in ll the head should
        # treverse  the entire list before we reach the desired node

        print("quality", quality)
        q  = quality
        print("q", q)
        print(q('B'))
        cur = self.head
        while cur is not None:
            if q(cur.data):
                print("cur.data", cur.data)
                return cur.data
            cur = cur.next


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        O(n) removing last element
        O(1) removing first element
        TODO: Worst case runn ing time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        cur = self.head
        if cur is not None and cur.data is item:
            if cur.next is None:
                self.tail = None
            self.head = cur.next
            cur = None
            return item
        prev = None
        while cur is not None and cur.data is not item:
            prev = cur
            cur = cur.next
        if cur is None:
            raise ValueError('Item not found: {}'.format(item))
            return item
        prev.next = cur.next
        if cur.next is None:
            self.tail = prev
        cur = None

def test_linked_list():
    ll = LinkedList()
    # print('list: {}'.format(ll))
    #
    # print('\nTesting append:')
    # for item in ['A', 'B', 'C', 'D', 1]:
    #     print('append({!r})'.format(item))
    #     ll.append(item)
    #     print('list: {}'.format(ll))
    #
    # ll = LinkedList(['A', 'B', 'C'])
    # ll.head.data == 'A'  # First item
    # ll.tail.data == 'C'  # Last item
    # ll.delete('A')
    # ll.head.data == 'B'  # New head
    # ll.tail.data == 'C'  # Unchanged
    # ll.delete('C')
    # ll.head.data == 'B'  # Unchanged
    # ll.tail.data == 'B'  # New tail
    # ll.delete('B')
    # ll.head is None  # No head
    # ll.tail is None  # No tail
    # # print('delete: {}'.format(ll.delete("D")))
    # print(ll.items())

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('head_node', ll.prepend("F"))
    # print('length: {}'.format(ll.length()))
    print('find: {}'.format(ll.find(lambda item: item == 'B')))
    # print(ll.items())
    print(ll.items())
    print('delete: {}'.format(ll.delete("J")))
    print(ll.items())




    # Enable this after implementing delete methd
    delete_implemented = False
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
