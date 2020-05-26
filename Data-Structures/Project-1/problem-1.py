class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache_max_size = capacity
        self.cache_size = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.cache_size == 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.is_empty():
            return -1

        node = self.head
        while node:
            if node.key == key:
                value = node.value
                self._update(node)
                return value
            node = node.next

        return -1

    def _update(self, node):
        """Updates the linked list based on recent calls"""
        if self.is_empty():
            return

        if node.prev == None:
            self.head.prev = self.tail
            self.tail.next = self.head
            self.head = self.head.next
            self.tail = self.tail.next
            self.head.prev = None
            self.tail.next = None
            return

        elif node.next == None:  # then this the tail node;

            return  # no update is required

        else:

            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node

            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next
            return

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.is_empty():

            self.head = Node(key, value)
            self.tail = self.head
            self.cache_size += 1

        elif self.cache_size == 1:

            self.tail = Node(key, value)
            self.tail.prev = self.head
            self.head.next = self.tail
            self.cache_size += 1

        elif self.cache_size < self.cache_max_size:

            new_node = Node(key, value)
            new_node.prev = self.tail
            self.tail = new_node
            new_node.prev.next = self.tail
            self.cache_size += 1

        elif self.cache_size == self.cache_max_size:

            self.head = self.head.next
            self.head.prev = None
            self.cache_size -= 1
            self.set(key, value)

    def __str__(self):
        output = ""
        if self.is_empty():
            return output
        else:
            node = self.tail
            while node:
                output += "({},{}) <-".format(str(node.key),str(node.value))
                node = node.prev
        return output



# ====================================
# ===== TEST
# ====================================
our_cache = LRU_Cache(5)
print(our_cache)
our_cache.set(1, 1);
print(our_cache)
our_cache.set(2, 2);
print(our_cache)
our_cache.set(3, 3);
print(our_cache)
our_cache.set(4, 4);
print(our_cache)

assert(our_cache.get(1) == 1)       # returns 1
print(our_cache)
assert(our_cache.get(2) == 2)      # returns 2
print(our_cache)
assert(our_cache.get(4) == 4)      # returns 4
print(our_cache)
assert(our_cache.get(9) == -1)      # returns -1 because 9 is not present in the cache
print(our_cache)
our_cache.set(5, 5)
print(our_cache)
our_cache.set(6, 6)
print(our_cache)
assert(our_cache.get(3) == -1)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache)
