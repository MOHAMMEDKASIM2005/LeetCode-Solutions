class Node:

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node()    # LRU side
        self.right = Node()   # MRU side

        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node
    def remove(self, node):

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # Insert at MRU side
    def insert(self, node):

        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key):

        # Key not present
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move node to MRU
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):

        # Key already exists
        if key in self.cache:
            self.remove(self.cache[key])

        # Create new node
        node = Node(key, value)

        # Store in HashMap
        self.cache[key] = node

        # Add to MRU
        self.insert(node)

        # Capacity exceeded
        if len(self.cache) > self.capacity:

            # First real node = LRU
            lru = self.left.next

            self.remove(lru)

            # Remove from HashMap
            del self.cache[lru.key]