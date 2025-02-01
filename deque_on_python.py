class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class Deque():
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        s = ""

        currrent = self.head.next
        while currrent.next:
            s += str(currrent.data)
            s += " "
            currrent = currrent.next

        return s[:-1]
    
    def push_front(self, data):
        node = Node(
            data=data
        )

        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node

        self.size += 1

    def push_back(self, data):
        node = Node(
            data=data
        )

        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

        self.size += 1

    def pop_front(self) -> any:
        if self.head.next == self.tail:
            return None
        
        result = self.head.next

        result.next.prev = self.head
        self.head.next = result.next
        self.size -= 1

        return result.data
        


    def pop_back(self) -> any:
        if self.head.next == self.tail:
            return None
        
        result = self.tail.prev

        result.prev.next = self.tail
        self.tail.prev = result.prev
        self.size -= 1

        return result.data

