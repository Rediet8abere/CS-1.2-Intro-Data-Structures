#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.count = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n^2)we have to loop through
        list of linked list n times to access the linkedlist,
        and n times to access the keys."""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n^2) we have to loop through
        list of linked list n times to access the linkedlist,
        and n times to access the values.
        """
        # Loop through all buckets
        # Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) bestcase and average case we have to loop through the list of linked
        list to get linked list """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items()) # puts the linked list in the same list
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(1) we're adding to count as soon as we add a key value pair?"""
        # return the count
        return self.count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: bestcase - O(1) if item is on the first bucket and head_node;
        average case - 0(n/b) after getting the bucket in 0(1) it looks through the
        linkedlist."""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket

        index = self._bucket_index(key)
        bucket = self.buckets[index]

        for key_bucket, value in bucket.items():
            if key_bucket == key:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: bestcase - O(1) if item is on the first bucket and head_node;
        average case - 0(n/b) after getting the bucket in 0(1) it looks through the
        linkedlist."""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, return value associated with given key
        # Otherwise, raise error to tell user get failed
        # raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for key_bucket, value in bucket.items():
            if key_bucket == key:
                return value
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: bestcase - O(1) if item is on the first bucket and head_node;
        average case - 0(n/b) after getting the bucket in 0(1) it looks through the
        linkedlist."""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, update value associated with given key
        # Otherwise, insert given key-value entry into bucket
        self.count += 1
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        print("printing bucket find: ", bucket.find(lambda item: (key, value)))
        if bucket.find(lambda item: (key, value)) is None:
            bucket.append((key, value))
            return
        self.delete(key)
        bucket.append((key, value))
        return


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: bestcase - O(1) if item is on the first bucket and head_node;
        average case - 0(n/b) after getting the bucket in 0(1) it looks through the
        linkedlist."""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        # If found, delete entry associated with given key
        # Otherwise, raise error to tell user delete failed
        # raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        for key_bucket, value in bucket.items():
            if key_bucket == key:
                bucket.delete((key_bucket, value))
                self.count -= 1
                print("self.buckets in delete", self.buckets)
                return

        raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 4), ('X', 9)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print("hash code", ht._bucket_index(key))
        print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('Mia', 1), ('Sue', 4)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print("hash code>>>>>>>>>>>>>>>>>>>>>>>>.", ht._bucket_index(key))
        print('hash table>>>>>>>>>>>>>>>>>>>>>>>>: {}'.format(ht))
    #
    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))
    #
    print("Testing set for updates")
    for key, value in [('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))
    print('\nTesting get:')
    for key in ['I', 'V']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))
    print("items: ", ht.items())

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
