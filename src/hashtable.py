# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.linked_list = LinkedList()

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = LinkedPair(key, value)
        bucket = self.storage[index]
        linked_list = LinkedList()
        # check if bucket is empty. If so, add pair as head node
        if bucket is None:
            # Create a head node
            new_node = LinkedPair(pair, linked_list.head)
            # Set current head to new node
            linked_list.head = new_node
        else:
            # check if key already exists in bucket
            current_node = linked_list.head
            while(current_node):
                if current_node.value.key == key:
                    current_node.value.value = value
                    return

                current_node = current_node.next

            # if new key, add to linked List as head
            new_node = LinkedPair(pair, linked_list.head)
            linked_list.head = new_node


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]
        #if pair:
        #    pair = None
        #else:
        #    print("WARNING: Key not found.")
        # If we have no head
        if not linked_list.head:
            # print an error and return
            print("Error: Value not found")
        # If the head has our value
        elif linked_list.head.value == value:
            # Remove the head by pointing self.head to head.next
            linked_list.head = linked_list.head.next
        # Else
        else:
            # Keep track of the parent node
            parent = linked_list.head
            current = linked_list.head.next
            # Walk through the linked list until we find a matching value
            while current:
                # If we find a matching value
                if current.value == value:
                    # Delete the node by pointing parent.next to node.next
                    parent.next = current.next
                    return

                current = current.next
            # If we get to the end and have not found the value, print error
            print("Error: Value not found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]

        current_node = self.linked_list.head

        while(current_node):
            if current_node.value.key == key:
                return current_node.value.value

            current_node = current_node.next

        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        # Copy old items to new storage
        for i in range(self.capacity):
            new_storage[i] = self.storage[i]
        # Point storage to the new storage
        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
